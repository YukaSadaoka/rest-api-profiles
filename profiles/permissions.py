from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, iew, obj):
        """Check user if they have permissions to edit the target profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return  obj.id == request.user.id