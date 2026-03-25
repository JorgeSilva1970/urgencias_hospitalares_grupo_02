# apps/faturacao/serializers.py

from rest_framework import serializers
from .models import Faturacao


class FaturacaoSerializer(serializers.ModelSerializer):
    """
    Serializer para faturação.
    """

    class Meta:
        model = Faturacao
        fields = "__all__"