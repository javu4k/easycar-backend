from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import PerfilCliente
from .serializers import UserSerializer, PerfilClienteSerializer
from .permissions import IsFuncionario

class UserViewSet(viewsets.ModelViewSet):
    """
    CRUD de Usuários.
    Apenas funcionários podem gerenciar usuários.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsFuncionario] 

class PerfilClienteViewSet(viewsets.ModelViewSet):
    """
    CRUD de Perfis de Clientes.
    Apenas funcionários cadastram e editam perfis de clientes.
    """
    queryset = PerfilCliente.objects.all()
    serializer_class = PerfilClienteSerializer
    permission_classes = [IsFuncionario]