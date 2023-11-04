from django.urls import path, include
from core.rest.views.users import UserList

urlpatterns = [
    path("", UserList.as_view(), name="user-list-create"),
]
