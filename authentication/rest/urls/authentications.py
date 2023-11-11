"""Url mapping for authentication api"""

from django.urls import path
from authentication.rest.views.authentications import RegistrationView, LoginView, ActiveAccountView

urlpatterns = [
    path("register", RegistrationView.as_view(), name="registration"),
    path("token", LoginView.as_view(), name="token"),
    path("active-account",ActiveAccountView.as_view(), name="activate-account")
]
