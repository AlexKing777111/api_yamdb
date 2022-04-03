from rest_framework import permissions


class ReviewCommentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return(
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return(
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
            # or .....
        )


class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return(
            request.method in permissions.SAFE_METHODS)


class AdminUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return(request.user.role == 'admin')

    def has_object_permission(self, request, view, obj):
        return(request.user.role == 'admin')
