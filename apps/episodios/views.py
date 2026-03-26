# apps/episodios/views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Hospital, EpisodioUrgencia, Triagem, Consulta, Prescricao
from .serializers import (
    HospitalSerializer,
    EpisodioUrgenciaSerializer,
    TriagemSerializer,
    ConsultaSerializer,
    PrescricaoSerializer,
)

from apps.common.permissions import IsProfissionalSaudeOuAdmin


class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all().order_by("nome")
    serializer_class = HospitalSerializer
    permission_classes = [IsAuthenticated]


class EpisodioUrgenciaViewSet(viewsets.ModelViewSet):
    queryset = EpisodioUrgencia.objects.all().order_by("-data_hora_entrada")
    serializer_class = EpisodioUrgenciaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()

        estado = self.request.query_params.get("estado")
        utente = self.request.query_params.get("utente")
        prioridade = self.request.query_params.get("prioridade")

        if estado:
            queryset = queryset.filter(estado_atual=estado)

        if utente:
            queryset = queryset.filter(utente_id=utente)

        if prioridade:
            queryset = queryset.filter(prioridade_manchester=prioridade)

        return queryset


class TriagemViewSet(viewsets.ModelViewSet):
    queryset = Triagem.objects.all().order_by("-data_hora_triagem")
    serializer_class = TriagemSerializer
    permission_classes = [IsProfissionalSaudeOuAdmin]


class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all().order_by("-data_hora")
    serializer_class = ConsultaSerializer
    permission_classes = [IsAuthenticated]
    

class PrescricaoViewSet(viewsets.ModelViewSet):
    queryset = Prescricao.objects.all().order_by("-data_hora")
    serializer_class = PrescricaoSerializer
    permission_classes = [IsProfissionalSaudeOuAdmin]


@api_view(["GET"])
@permission_classes([IsProfissionalSaudeOuAdmin])
def painel_triagem(request):
    """
    Painel de triagem para visualizar episódios em curso.
    """

    episodios = EpisodioUrgencia.objects.filter(
        fechado=False
    ).select_related(
        "utente",
        "medico_responsavel",
        "enfermeiro_responsavel"
    ).order_by("data_hora_entrada")

    dados = []

    prioridade_ordem = {
        "VERMELHO": 1,
        "LARANJA": 2,
        "AMARELO": 3,
        "VERDE": 4,
        "AZUL": 5,
    }

    for episodio in episodios:
        dados.append({
            "episodio_id": episodio.id,
            "utente_id": episodio.utente.id,
            "nome_utente": episodio.utente.nome,
            "numero_utente": episodio.utente.numero_utente,
            "data_hora_entrada": episodio.data_hora_entrada,
            "prioridade_manchester": episodio.prioridade_manchester,
            "estado_atual": episodio.estado_atual,
            "motivo_admissao": episodio.motivo_admissao,
            "tempo_decorrido_minutos": episodio.tempo_decorrido_minutos,
            "medico_responsavel": (
                episodio.medico_responsavel.username
                if episodio.medico_responsavel else None
            ),
            "enfermeiro_responsavel": (
                episodio.enfermeiro_responsavel.username
                if episodio.enfermeiro_responsavel else None
            ),
            "ordem_prioridade": prioridade_ordem.get(
                episodio.prioridade_manchester, 99
            ),
        })

    dados.sort(key=lambda x: (x["ordem_prioridade"], x["data_hora_entrada"]))
    return Response(dados)