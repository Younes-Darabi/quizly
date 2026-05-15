from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of a quiz to access or modify it.
    """
    def has_object_permission(self, request, view, obj):
        """
        Returns True if the requesting user is the owner of the object.
        """
        return request.user == obj.user
