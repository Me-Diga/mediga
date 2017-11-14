from user.models import UserProfile
from django.contrib.auth.models import User
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.views.generic import View


class HomepageView(View):
    http_method_names = [u'get']

    def get(self, request):
        current_user = request.user
        current_profile = None
        if not current_user.is_anonymous():
            current_profile = UserProfile.objects.get(user=current_user)

        response = render(request, 'homepage.html', {
            'current_profile': current_profile
        })

        return response


class SearchView(View):
    http_method_names = [u'get']

    def get(self, request):
        current_user = request.user
        current_profile = None
        if not current_user.is_anonymous():
            current_profile = UserProfile.objects.get(user=current_user)

        query = request.GET.get('query')

        username_list = []
        first_name_list = []
        last_name_list = []
        profile_list = []

        for user in User.objects.filter(username__icontains=query):
            username_list.append(user)

        for user in User.objects.filter(first_name__icontains=query):
            first_name_list.append(user)

        for user in User.objects.filter(last_name__icontains=query):
            last_name_list.append(user)

        for user in username_list:
            profile = UserProfile.objects.get(user=user)
            if profile not in profile_list:
                profile_list.append(profile)

        for user in first_name_list:
            profile = UserProfile.objects.get(user=user)
            if profile not in profile_list:
                profile_list.append(profile)

        for user in last_name_list:
            profile = UserProfile.objects.get(user=user)
            if profile not in profile_list:
                profile_list.append(profile)

        paginator = Paginator(profile_list, 4)

        page = request.GET.get('page')
        try:
            profiles = paginator.page(page)
        except PageNotAnInteger:
            profiles = paginator.page(1)
        except EmptyPage:
            profiles = paginator.page(paginator.num_pages)

        response = render(request, 'search.html', {
            'current_profile': current_profile,
            'query': query,
            'paginator': paginator,
            'profiles': profiles
        })

        return response
