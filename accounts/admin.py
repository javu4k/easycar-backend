from django.contrib import admin
from .models import PerfilCliente

@admin.register(PerfilCliente)
class PerfilClienteAdmin(admin.ModelAdmin):
    list_display = ('user', 'cnh', 'telefone')
    search_fields = ('user__username', 'cnh')