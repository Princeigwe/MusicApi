from rest_framework import permissions

class PlaylistOwnerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated or request.user.is_superuser:
            return True
    def has_object_permission(self, request, view, obj):
        if obj.user == request.user or request.user.is_superuser:
            return True