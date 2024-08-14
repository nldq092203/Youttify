from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div
from django_registration.forms import RegistrationForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from youttify_auth.models import YouttifyUser


class YouttifyAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Email address")
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")

    def __init__(self, *args, **kwargs):
        super(YouttifyAuthenticationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'login'
        self.helper.layout = Layout(
            Field('username', 
                  css_class='border border-secondary form-control form-control-lg',
                  placeholder='Enter a valid email address', 
                  id='form_email'),
            Field('password', 
                  css_class='border border-secondary form-control form-control-lg',
                  placeholder='Enter password', 
                  id='form_password'),
            Submit('submit', 'Login', css_class='btn btn-primary btn-lg'),
        )
    

class YouttifyRegistrationForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = YouttifyUser
        fields = ['email']

    email = forms.EmailField(label="Email address")
    password1 = forms.CharField(widget=forms.PasswordInput(), label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

    def __init__(self, *args, **kwargs):
        super(YouttifyRegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.error_class = 'is-invalid'
        self.helper.form_method = 'post'
        self.helper.form_action = 'django_registration_register'
        self.helper.layout = Layout(
            Div(
                Field('email',
                      css_class='border border-secondary form-control form-control-lg',
                      placeholder='Enter your email address',
                      id='form_email',),
                css_class='form-group'
            ),
            Div(
                Field('password1',
                      css_class='border border-secondary form-control form-control-lg',
                      placeholder='Enter a password',
                      id='form_password1',),
                css_class='form-group'
            ),
            Div(
                Field('password2',
                      css_class='border border-secondary form-control form-control-lg',
                      placeholder='Confirm your password',
                      id='form_password2',),
                css_class='form-group'
            ),
            Div(
                Submit('submit', 'Register', css_class='btn btn-primary btn-lg'),
                css_class='form-group'
            )
        )