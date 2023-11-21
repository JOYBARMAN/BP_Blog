from django.urls import path
from post.rest.views.posts import AdminPostList, UserPostList

urlpatterns = [
    path("", UserPostList.as_view(), name="user-post-list"),
    path("/admin", AdminPostList.as_view(), name="admin-post-list"),
]
