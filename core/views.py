from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from rest_framework.decorators import action # IMPORT NECESSÁRIA PARA O @action
from rest_framework.response import Response # IMPORT NECESSÁRIA PARA RETORNAR RESPOSTAS PERSONALIZADAS
from .models import Carro, Aluguel, PerfilCliente # Certifique-se de que PerfilCliente está no seu models.py ou importado corretamente. Se estiver em outro app, ajuste a importação.
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

        from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import PerfilCliente # Certifique-se que PerfilCliente está importado aqui ou na linha 1

# ... (Mantenha as classes CarroViewSet e AluguelViewSet que já fizemos)

# Nova ViewSet para rotas personalizadas
class RotasEspecificasViewSet(viewsets.GenericViewSet):
    # Não precisa de queryset base, pois as ações serão personalizadas
    
    # 1. Rota: /api/me/alugueis/
    @action(detail=False, methods=['get'], url_path='me/alugueis', 
            permission_classes=[permissions.IsAuthenticated])
    def meus_alugueis(self, request):
        user = request.user
        if not user.is_staff and user.groups.filter(name='Clientes').exists():
            try:
                perfil = user.perfilcliente # Supondo related_name 'perfilcliente'
                queryset = Aluguel.objects.filter(perfil_cliente=perfil)
                serializer = AluguelSerializer(queryset, many=True)
                return Response(serializer.data)
            except PerfilCliente.DoesNotExist:
                return Response({'detail': 'Perfil de cliente não encontrado.'}, status=404)
        
        # Se não for cliente, ele pode ver tudo (embora a rota seja específica para 'me')
        # Podemos retornar erro ou, se for funcionário, redirecionar para todos os alugueis
        return Response({'detail': 'Acesso negado para esta rota exclusiva de cliente.'}, status=403)


    # 2. Rota: /api/funcionarios/{id}/alugueis/
    @action(detail=True, methods=['get'], url_path='alugueis', 
            permission_classes=[permissions.IsAdminUser]) # Apenas Admin/Funcionário pode usar
    def alugueis_por_funcionario(self, request, pk=None):
        funcionario = get_object_or_404(User, pk=pk)
        
        # Filtra aluguéis registrados apenas por esse funcionário
        queryset = Aluguel.objects.filter(funcionario=funcionario)
        serializer = AluguelSerializer(queryset, many=True)
        return Response(serializer.data)