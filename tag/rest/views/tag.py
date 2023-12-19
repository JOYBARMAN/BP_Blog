"""Views for tag"""

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from tag.models import Tag
from tag.rest.serializers.tag import TagListSerializer, TagDetailSerializer
from core.permissions import IsAuthenticated, IsAdminUser, SAFE_METHODS


class TagList(ListCreateAPIView):
    """Api for tag list and create"""

    queryset = Tag().get_all_actives()
    serializer_class = TagListSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated()]
        else:
            return [IsAdminUser()]


class TagDetail(RetrieveUpdateAPIView):
    """Api for tag retrieve and update"""

    queryset = Tag().get_all_actives()
    serializer_class = TagDetailSerializer
    lookup_field = "uid"

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated()]
        else:
            return [IsAdminUser()]
