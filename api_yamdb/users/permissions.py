from rest_framework import permissions


class AdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role == "admin"
        return False

    def has_object_permission(self, request, view, obj):
        return request.user.role == "admin"


class AdminSuperuser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return True
