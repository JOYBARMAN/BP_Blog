from django.urls import path
from sub_category.rest.views.sub_category import SubCategoryList, SubCategoryDetail

urlpatterns = [
    path("", SubCategoryList.as_view(), name="subcategory-list-create"),
    path("/<uuid:uid>", SubCategoryDetail.as_view(), name="subcategory-details"),
]
