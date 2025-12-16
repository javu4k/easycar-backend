from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Carro, Aluguel
from .serializers import CarroSerializer, AluguelSerializer

# Permissão personalizada: Só funcionário pode alterar (clientes apenas leem)
class IsFuncionarioOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff or request.user.groups.filter(name='Funcionarios').exists()

class CarroViewSet(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
    permission_classes = [permissions.IsAuthenticated, IsFuncionarioOrReadOnly]

class AluguelViewSet(viewsets.ModelViewSet):
    serializer_class = AluguelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Se for funcionário, vê todos os aluguéis
        if user.is_staff or user.groups.filter(name='Funcionarios').exists():
            return Aluguel.objects.all()
        # Se for cliente, vê apenas os seus
        # Supõe que o usuário logado tem um perfil_cliente associado
        if hasattr(user, 'perfilcliente'):
            return Aluguel.objects.filter(perfil_cliente=user.perfilcliente)
        return Aluguel.objects.none()

    def perform_create(self, serializer):
        # Registra quem criou o aluguel (o funcionário logado)
        serializer.save(funcionario=self.request.user)