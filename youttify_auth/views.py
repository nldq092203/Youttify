from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django_registration.backends.activation.views import RegistrationView
from django.shortcuts import resolve_url
from youttify_auth.forms import YouttifyAuthenticationForm, YouttifyRegistrationForm



class Login(LoginView):
    template_name = "youttify_auth/registration/login.html"
    redirect_authenticated_user = True
    authentication_form = YouttifyAuthenticationForm

    def get_success_url(self) -> str:
        #Check of 'next' parameter is in the request
        next_url = self.request.GET.get('next')
        if next_url:
            return resolve_url(next_url)
        return '/home/'

class Logout(LogoutView):
    template_name = "youttify_auth/registration/logged_out.html"
