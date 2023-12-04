"""Urls for post reaction"""

from django.urls import path
from post_reaction.rest.views.post_reaction import PostReactionCount

urlpatterns = [
    path(
        "/count", PostReactionCount.as_view(), name="user-post-reaction-count"
    ),
]
