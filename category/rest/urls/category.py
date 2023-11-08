from django.urls import path
from category.rest.views.category import CategoryList, CategoryDetail

urlpatterns = [
    path("", CategoryList.as_view(), name="category-list-create"),
    path("/<uuid:uid>", CategoryDetail.as_view(), name="category-details"),
]
