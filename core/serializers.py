from rest_framework import serializers
from .models import Carro, Aluguel

class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = '__all__'

class AluguelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluguel
        fields = '__all__'
        read_only_fields = ['funcionario'] # O funcionário é preenchido automaticamente