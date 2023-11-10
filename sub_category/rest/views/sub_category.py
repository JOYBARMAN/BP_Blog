"""Views for subcategory"""

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from sub_category.models import SubCategory
from sub_category.rest.serializers.sub_category import (
    SubCategoryListSerializer,
    SubCategoryPostSerializer,
)
from core.permissions import (
    IsAuthenticated,
    IsAdminUser,
    SAFE_METHODS,
)


class SubCategoryList(ListCreateAPIView):
    queryset = SubCategory().get_all_actives().select_related("category")

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return SubCategoryListSerializer
        else:
            return SubCategoryPostSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated()]
        else:
            return [IsAdminUser()]


class SubCategoryDetail(RetrieveUpdateAPIView):
    queryset = SubCategoryList.queryset
    lookup_field = "uid"

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return SubCategoryListSerializer
        else:
            return SubCategoryPostSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated()]
        else:
            return [IsAdminUser()]
