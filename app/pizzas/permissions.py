from rest_framework import permissions


class StaffOrSuperuserPermission(permissions.BasePermission):
    """
    Permiso personalizado para otorgar acceso usuarios autenticados que sean
    staff o superusuario.
    """
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            (request.user.is_staff or request.user.is_superuser)
        )
