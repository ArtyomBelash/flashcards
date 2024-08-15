from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsOwnerOrAdminOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if obj.owner == request.user:
            return True
        return bool(request.user.is_staff)
