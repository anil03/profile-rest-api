from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allows user to edit own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        """SAFE_METHODS : Create a New user & View"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class PostOwnStatus(permissions.BasePermission):
    """Allows user to post their own status"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own status"""
        """SAFE_METHODS : Create a New user & View"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id

