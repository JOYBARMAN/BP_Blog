from django.urls import path
from tag.rest.views.tag import TagList, TagDetail

urlpatterns = [
    path("", TagList.as_view(), name="tag-list-create"),
    path("/<uuid:uid>", TagDetail.as_view(), name="tag-detail-update"),
]
