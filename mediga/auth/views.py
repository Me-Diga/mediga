from auth.forms import UserLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views.generic.edit import FormView


class UserLoginView(FormView):
    """
    Class for User login view.
    """
    http_method_names = [u'get', u'post']

    def get(self, request):
        current_user = request.user

        if current_user.is_anonymous():
            form = UserLoginForm()
            response = render(request, 'sign_in.html', {'form': form})
        else:
            response = redirect('/')

        return response

    def post(self, request):
        form = UserLoginForm(request.POST)

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            response = redirect('/')
        else:
            messages.error(request, 'Nome de usuário e/ou senha incorreto(s).')
            response = render(request, 'sign_in.html', {'form': form})

        return response


class UserLogoutView(FormView):
    """
    Class for User logout view.
    """
    http_method_names = [u'get']

    def get(self, request):
        current_user = request.user

        if current_user.is_authenticated():
            logout(request)
            response = redirect('/')
        else:
            response = redirect('/')

        return response
