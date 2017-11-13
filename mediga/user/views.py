from user.forms import UserProfileCreateForm
from user.models import UserProfile
from django.contrib.auth.models import User
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render
from django.views.generic import View
from django.views.generic.edit import FormView
from message.models import Message, Response


class UserProfileCreateView(FormView):
    """
    Class for User registration view.
    """
    http_method_names = [u'get', u'post']

    def get(self, request):
        current_user = request.user

        if current_user.is_anonymous():
            form = UserProfileCreateForm()
            response = render(request, 'sign_up.html', {'form': form})
        else:
            response = redirect('/')

        return response

    def post(self, request):
        form = UserProfileCreateForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            profile = UserProfile.objects.create(
                user=user,
                avatar=form.cleaned_data['avatar']
            )
            profile.save()

            response = redirect('/')
        else:
            response = render(request, 'sign_up.html', {'form': form})

        return response


class UserProfileView(View):
    http_method_names = [u'get']

    def get(self, request, username):
        current_user = request.user
        current_profile = None
        if not current_user.is_anonymous():
            current_profile = UserProfile.objects.get(user=current_user)

        main_user = User.objects.get(username=username)
        main_profile = UserProfile.objects.get(user=main_user)

        messages_list = []

        for message in main_profile.received_messages.all():
            if message.published:
                messages_list.append(message)

        messages_list.sort(key=lambda r: r.created_at, reverse=True)

        paginator = Paginator(messages_list, 5)

        page = request.GET.get('page')
        try:
            messages = paginator.page(page)
        except PageNotAnInteger:
            messages = paginator.page(1)
        except EmptyPage:
            messages = paginator.page(paginator.num_pages)

        response = render(request, 'profile.html', {
            'current_profile': current_profile,
            'main_profile': main_profile,
            'paginator': paginator,
            'messages': messages
        })

        return response

    def new_message(request, username):
        page = request.GET.get('page')
        body = request.POST.get('message')
        message_style = request.POST.get('message_style')

        if message_style == 'not_anonymous':
            anonymous = False
            current_user = request.user
            current_profile = UserProfile.objects.get(user=current_user)
        elif message_style == 'anonymous':
            anonymous = True

        main_user = User.objects.get(username=username)
        main_profile = UserProfile.objects.get(user=main_user)

        if anonymous:
            Message.objects.create(
                body=body,
                receiver=main_profile
            )
        else:
            Message.objects.create(
                body=body,
                receiver=main_profile,
                author=current_profile
            )

        main_profile.unread_messages = main_profile.unread_messages + 1
        main_profile.save()

        response = redirect('/user/{}?page={}'.format(username, page))

        return response

    def new_response(request, username, message_pk):
        page = request.GET.get('page')
        body = request.POST.get('response')

        current_user = request.user
        current_profile = UserProfile.objects.get(user=current_user)

        message = Message.objects.get(pk=message_pk)

        if current_user.username == username or\
            current_user.username == message.author.user.username:

            response = Response.objects.create(
                body=body,
                message=message,
                author=current_profile
            )

        response = redirect('/user/{}?page={}'.format(username, page))

        return response

    def delete_published_message(request, username, message_pk):
        page = request.GET.get('page')

        current_user = request.user

        if current_user.username == username:
            message = Message.objects.get(pk=message_pk)
            message.delete()
            response = redirect('/user/{}?page={}'.format(username, page))
        else:
            response = redirect('/')

        return response

    def delete_response(request, username, response_pk):
        page = request.GET.get('page')

        current_user = request.user

        if current_user.username == username:
            response_obj = Response.objects.get(pk=response_pk)
            response_obj.delete()
            response = redirect('/user/{}?page={}'.format(username, page))
        else:
            response = redirect('/')

        return response


class UserBoxView(View):
    http_method_names = [u'get']

    def get(self, request, username):
        current_user = request.user
        current_profile = None
        if not current_user.is_anonymous():
            current_profile = UserProfile.objects.get(user=current_user)

        if current_user.username == username:

            messages_list = []

            for message in current_profile.received_messages.all():
                if not message.published:
                    messages_list.append(message)

            messages_list.sort(key=lambda r: r.created_at, reverse=True)

            paginator = Paginator(messages_list, 5)

            page = request.GET.get('page')
            try:
                messages = paginator.page(page)
            except PageNotAnInteger:
                messages = paginator.page(1)
            except EmptyPage:
                messages = paginator.page(paginator.num_pages)

            current_profile.unread_messages = 0
            current_profile.save()

            response = render(request, 'box.html', {
                'current_profile': current_profile,
                'paginator': paginator,
                'messages': messages
            })

        else:
            response = redirect('/user/{}'.format(username))

        return response

    def delete_box_message(request, username, message_pk):
        page = request.GET.get('page')

        current_user = request.user

        if current_user.username == username:
            message = Message.objects.get(pk=message_pk)
            message.delete()
            response = redirect('/user/{}/box?page={}'.format(username, page))
        else:
            response = redirect('/')

        return response

    def publish_message(request, username, message_pk):
        page = request.GET.get('page')

        current_user = request.user

        if current_user.username == username:
            message = Message.objects.get(pk=message_pk)
            message.published = True
            message.save()
            response = redirect('/user/{}/box?page={}'.format(username, page))
        else:
            response = redirect('/')

        return response
