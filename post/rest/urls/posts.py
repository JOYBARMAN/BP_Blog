from django.urls import path
from post.rest.views.posts import AdminPostList

urlpatterns = [
    path("/admin", AdminPostList.as_view(), name="admin-post-list"),
]