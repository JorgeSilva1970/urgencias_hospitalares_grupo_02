# apps/common/permissions.py

from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """
    Permissão para utilizadores com perfil de administrador.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            getattr(request.user, "tipo_profissional", None) == "ADMIN"
        )


class IsMedico(BasePermission):
    """
    Permissão para médicos.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            getattr(request.user, "tipo_profissional", None) == "MEDICO"
        )


class IsEnfermeiro(BasePermission):
    """
    Permissão para enfermeiros.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            getattr(request.user, "tipo_profissional", None) == "ENFERMEIRO"
        )


class IsRececionistaOuAdmin(BasePermission):
    """
    Permite acesso a rececionistas e administradores.
    Útil para registo de entrada e dados administrativos.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            getattr(request.user, "tipo_profissional", None) in ["RECECIONISTA", "ADMIN", "ADMINISTRATIVO"]
        )


class IsProfissionalSaudeOuAdmin(BasePermission):
    """
    Permite acesso a médico, enfermeiro ou administrador.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            getattr(request.user, "tipo_profissional", None) in ["MEDICO", "ENFERMEIRO", "ADMIN"]
        )