from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

# Importando as views que criamos
from accounts.views import UserViewSet, PerfilClienteViewSet

# Importando as views 
from core.views import CarroViewSet, AluguelViewSet, RotasEspecificasViewSet

# Configurando o roteador 
router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'perfis-clientes', PerfilClienteViewSet)

router.register(r'carros', CarroViewSet, basename='carro')
router.register(r'alugueis', AluguelViewSet, basename='aluguel')

# Rotas Personalizadas (que vão gerar /api/rotas-especificas/me/alugueis/)
router.register(r'rotas-especificas', RotasEspecificasViewSet, basename='rotas-especificas')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rota Principal da API
    path('api/', include(router.urls)),

    # Autenticação (Login para pegar o Token)
    path('api/auth/token/', obtain_auth_token, name='api_token_auth'),

    # Documentação Swagger e Redoc
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]