from rest_framework import permissions


class ReviewCommentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
            or request.user.is_authenticated
            and request.user.role == "admin"
            or request.user.is_authenticated
            and request.user.role == "moderator"
        )


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class AdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role == "admin"
        return False

    def has_object_permission(self, request, view, obj):
        return request.user.role == "admin"
