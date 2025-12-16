from django.db import models
from django.contrib.auth.models import User
from accounts.models import PerfilCliente 

class Carro(models.Model):
    STATUS_CHOICES = [
        ('DISPONIVEL', 'Disponível'),
        ('ALUGADO', 'Alugado'),
        ('MANUTENCAO', 'Em Manutenção'),
    ]

    modelo = models.CharField(max_length=100)
    placa = models.CharField(max_length=10, unique=True)
    ano = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DISPONIVEL')

    def __str__(self):
        return f"{self.modelo} ({self.placa})"

class Aluguel(models.Model):
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE, related_name='alugueis')
    perfil_cliente = models.ForeignKey(PerfilCliente, on_delete=models.CASCADE, related_name='alugueis')
    funcionario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='alugueis_realizados')
    
    data_inicio = models.DateField()
    data_fim = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Aluguel {self.carro} - {self.perfil_cliente}"