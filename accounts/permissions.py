from rest_framework import permissions

class IsFuncionario(permissions.BasePermission):

    #permite acesso apenas a usuários do grupo Funcionários ou Superusuários

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        return request.user.groups.filter(name='Funcionários').exists() or request.user.is_superuser

class IsCliente(permissions.BasePermission):

    #permite acesso apenas a usuários do grupo Clientes

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        return request.user.groups.filter(name='Clientes').exists()