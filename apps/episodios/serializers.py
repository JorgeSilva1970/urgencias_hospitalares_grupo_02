# apps/episodios/serializers.py

from rest_framework import serializers
from .models import (
    Hospital,
    EpisodioUrgencia,
    Triagem,
    Consulta,
    Prescricao,
)


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = "__all__"


class EpisodioUrgenciaSerializer(serializers.ModelSerializer):
    tempo_decorrido_minutos = serializers.ReadOnlyField()

    class Meta:
        model = EpisodioUrgencia
        fields = "__all__"


class TriagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Triagem
        fields = "__all__"


class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = "__all__"


class PrescricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescricao
        fields = "__all__"