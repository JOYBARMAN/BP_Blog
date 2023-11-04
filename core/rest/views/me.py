from rest_framework.generics import RetrieveUpdateAPIView

from common.renderers import ErrorRenderers
from core.permissions import IsAuthenticated
from core.rest.serializers.users import UserListSerializer


class MeDetail(RetrieveUpdateAPIView):
    """Views to me detail and update"""

    serializer_class = UserListSerializer
    permission_classes = (IsAuthenticated,)
    # renderer_classes = [ErrorRenderers]

    def get_object(self):
        return self.request.user
