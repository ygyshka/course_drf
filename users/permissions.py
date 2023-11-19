from rest_framework.permissions import BasePermission


class IsStaff(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return False


class IsSuperUser(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False
