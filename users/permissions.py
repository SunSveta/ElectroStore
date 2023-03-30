from rest_framework.permissions import BasePermission


class ActiveUser(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return request.user.is_active
