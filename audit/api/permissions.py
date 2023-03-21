from rest_framework.permissions import BasePermission


class IsAuditor(BasePermission):
    """
    Allows access only to auditors.
    """

    def has_permission(self, request, view):
        return bool(
            request.user and request.user.groups.filter(name="auditor").exists()
        )
