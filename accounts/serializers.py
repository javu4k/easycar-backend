from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import PerfilCliente

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'groups']

    def create(self, validated_data):
        groups_data = validated_data.pop('groups', [])
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        if groups_data:
            user.groups.set(groups_data)
        return user

class PerfilClienteSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = PerfilCliente
        fields = '__all__'