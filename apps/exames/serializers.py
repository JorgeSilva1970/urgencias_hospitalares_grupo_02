# apps/exames/serializers.py

from rest_framework import serializers
from .models import Exame


class ExameSerializer(serializers.ModelSerializer):
    """
    Serializer para exames.
    """

    class Meta:
        model = Exame
        fields = "__all__"