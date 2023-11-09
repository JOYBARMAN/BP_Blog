"""Views for category"""
from django.db.models import Prefetch

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from category.models import Category
from sub_category.models import SubCategory
from category.rest.serializers.category import (
    CategoryListSerializer,
)
from core.permissions import (
    IsAuthenticated,
    IsAdminUser,
    SAFE_METHODS,
)


class CategoryList(ListCreateAPIView):
    serializer_class = CategoryListSerializer

    def get_queryset(self):
        return (
            Category()
            .get_all_actives()
            .filter()
            .prefetch_related(
                Prefetch(
                    "category",
                    queryset=SubCategory().get_all_actives(),
                    to_attr="sub_categories",
                )
            )
        )

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated()]
        else:
            return [IsAdminUser()]


class CategoryDetail(RetrieveUpdateAPIView):
    serializer_class = CategoryListSerializer
    lookup_field = "uid"

    def get_object(self):
        return CategoryList().get_queryset().get(uid=self.kwargs.get("uid"))

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated()]
        else:
            return [IsAdminUser()]
