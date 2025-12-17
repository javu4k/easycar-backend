from django.db import models
from django.contrib.auth.models import User

class PerfilCliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfilcliente') 
    cnh = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return f"Perfil de {self.user.username} - {self.cnh}"

    class Meta:
        verbose_name = "Perfil de Cliente"
        verbose_name_plural = "Perfis de Clientes"