"""Views for category"""

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from category.models import Category
from category.rest.serializers.category import (
    CategoryListSerializer,
)
from core.permissions import (
    IsAuthenticated,
    IsAdminUser,
    SAFE_METHODS,
)


class CategoryList(ListCreateAPIView):
    queryset = Category().get_all_actives()
    serializer_class = CategoryListSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated()]
        else:
            return [IsAdminUser()]


class CategoryDetail(RetrieveUpdateAPIView):
    queryset = Category().get_all_actives()
    serializer_class = CategoryListSerializer
    lookup_field = "uid"

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated()]
        else:
            return [IsAdminUser()]
