# apps/users/serializers.py

from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer para mostrar utilizadores.
    """

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "tipo_profissional",
            "numero_mecanografico",
        ]