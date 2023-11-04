"""Permission for core app """

from rest_framework.permissions import IsAuthenticated


class IsAdminUser(IsAuthenticated):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)
