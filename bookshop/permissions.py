from rest_framework.permissions import BasePermission, SAFE_METHODS
from bookshop.models import BlockUserModel


class BlocklistPermission(BasePermission):
    """
    Global permission check for blocked IPs.
    """

    def has_permission(self, request, view):
        user = request.user
        blocked = BlockUserModel.objects.filter(user=user).exists()
        return not blocked
