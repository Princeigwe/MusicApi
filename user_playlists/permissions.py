from rest_framework import permissions

class PlaylistOwnerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated or request.user.is_superuser:
            return True
    def has_object_permission(self, request, view, obj):
        if obj.user == request.user or request.user.is_superuser:
            return True

class PlaylistSongOwnerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated or request.user.is_superuser:
            return True
    def has_object_permission(self, request, view, obj):
        if obj.user_playlist.user == request.user or request.user.is_superuser:
            return True


class FavouritesOwnerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated or request.user.is_superuser:
            return True
    def has_object_permission(self, request, view, obj):
        if obj.user_playlist.user == request.user or request.user.is_superuser:
            return True