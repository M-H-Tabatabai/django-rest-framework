from rest_framework import permissions
from bookshop.models import BlockUserModel


class BlocklistPermission(permissions.BasePermission):
    """
    Global permission check for blocked IPs.
    """

    def has_permission(self, request, view):
        user = request.user
        blocked = BlockUserModel.objects.filter(user=user).exists()
        return not blocked
