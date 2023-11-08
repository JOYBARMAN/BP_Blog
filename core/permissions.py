"""Permission for core app """

from rest_framework.permissions import BasePermission


SAFE_METHODS = ("GET", "HEAD", "OPTIONS")


class IsAuthenticated(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)


class IsAdminUser(IsAuthenticated):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)
