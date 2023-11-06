from django.urls import path
from authentication.rest.views.authentications import RegistrationView

urlpatterns = [
    path("register", RegistrationView.as_view(), name="registration"),
]
