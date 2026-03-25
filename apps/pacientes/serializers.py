# apps/pacientes/serializers.py

from rest_framework import serializers
from .models import Utente


class UtenteSerializer(serializers.ModelSerializer):
    """
    Serializer principal do utente.
    """

    class Meta:
        model = Utente
        fields = "__all__"