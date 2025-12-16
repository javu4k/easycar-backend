from django.contrib import admin
from .models import Carro, Aluguel

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'placa', 'ano', 'status')
    list_filter = ('status',)
    search_fields = ('modelo', 'placa')

@admin.register(Aluguel)
class AluguelAdmin(admin.ModelAdmin):
    list_display = ('carro', 'perfil_cliente', 'data_inicio', 'data_fim', 'valor')
    list_filter = ('data_inicio',)