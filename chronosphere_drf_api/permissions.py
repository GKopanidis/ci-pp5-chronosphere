from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permission class to ensure that only the owner of an object can edit it.
    """
    def has_object_permission(self, request, view, obj):
        """
        Check if the user has permission to edit the object.

        :param request: The HTTP request object.
        :param view: The view handling the request.
        :param obj: The object to check permissions on.
        :return: True if the user is allowed to edit the object,
                 False otherwise.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
