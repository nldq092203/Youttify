from django.urls import path
from youttify_auth import views
from django.contrib.auth import views as auth_views
from youttify_auth.forms import YouttifyRegistrationForm
from django_registration.backends.activation.views import RegistrationView, ActivationView
from django.views.generic import TemplateView


urlpatterns = [
    path('login/',  views.Login.as_view(), name="login"),
    path('logout/', views.Logout.as_view(), name="logout"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='youttify_auth/registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='youttify_auth/registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='youttify_auth/registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='youttify_auth/registration/password_reset_complete.html'), name='password_reset_complete'),
    path(
        "register/",
        RegistrationView.as_view(
            form_class=YouttifyRegistrationForm, 
            template_name='youttify_auth/django_registration/registration_form.html',
            email_subject_template='youttify_auth/django_registration/activation_email_subject.txt',
            email_body_template = 'youttify_auth/django_registration/activation_email_body.txt'
            ),
        name="django_registration_register",
    ),
    path('register/complete/', TemplateView.as_view(
        template_name='youttify_auth/django_registration/registration_complete.html'
    ), name='django_registration_complete'),
    path('activate/complete/', TemplateView.as_view(
        template_name='youttify_auth/django_registration/activation_complete.html'
    ), name='django_registration_activation_complete'),
    path('activate/<activation_key>/', ActivationView.as_view(
        template_name='youttify_auth/django_registration/activation_failed.html'
    ), name='django_registration_activate'),
    path('register/closed/', TemplateView.as_view(
        template_name='youttify_auth/django_registration/registration_closed.html'
    ), name='django_registration_disallowed'),

]