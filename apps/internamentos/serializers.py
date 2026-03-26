# apps/internamentos/serializers.py

from rest_framework import serializers
from .models import Internamento, ResumoDiarioInternamento


class ResumoDiarioInternamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumoDiarioInternamento
        fields = "__all__"


class InternamentoSerializer(serializers.ModelSerializer):
    numero_dias_internado = serializers.ReadOnlyField()

    class Meta:
        model = Internamento
        fields = "__all__"