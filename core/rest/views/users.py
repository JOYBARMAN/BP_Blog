from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from core.permissions import IsAdminUser
from core.models import User
from core.rest.serializers.users import UserListSerializer


class UserList(ListCreateAPIView):
    """Views for admin add and get users"""

    serializer_class = UserListSerializer
    permission_classes = [
        IsAdminUser,
    ]
    queryset = User().get_all_actives()
