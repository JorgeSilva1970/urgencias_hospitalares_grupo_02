# apps/faturacao/views.py

import csv
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Faturacao
from .serializers import FaturacaoSerializer
from .services import MonitorizacaoAdministrativaService

from apps.common.permissions import IsRececionistaOuAdmin
from apps.common.utils import anonimizar_utente_dict


class FaturacaoViewSet(viewsets.ModelViewSet):
    """
    CRUD de faturação.
    """

    queryset = Faturacao.objects.all().order_by("-data_registo")
    serializer_class = FaturacaoSerializer
    permission_classes = [IsRececionistaOuAdmin]

    def get_queryset(self):
        queryset = super().get_queryset()
        episodio = self.request.query_params.get("episodio")
        pago = self.request.query_params.get("pago")

        if episodio:
            queryset = queryset.filter(episodio_id=episodio)

        if pago is not None:
            if pago.lower() == "true":
                queryset = queryset.filter(pago=True)
            elif pago.lower() == "false":
                queryset = queryset.filter(pago=False)

        return queryset


@api_view(["GET"])
@permission_classes([IsRececionistaOuAdmin])
def monitorizacao_administrativa(request, utente_id):
    """
    Endpoint da área administrativa para monitorização do utente.
    """
    dados = MonitorizacaoAdministrativaService.consultar_monitorizacao_utente(utente_id)

    if not dados:
        return Response(
            {"detail": "Utente não encontrado."},
            status=status.HTTP_404_NOT_FOUND
        )

    return Response(dados, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsRececionistaOuAdmin])
def monitorizacao_administrativa_anonimizada(request, utente_id):
    """
    Devolve versão anonimizada da monitorização administrativa.
    Útil para análise, auditoria técnica e preparação para IA.
    """
    dados = MonitorizacaoAdministrativaService.consultar_monitorizacao_utente(utente_id)

    if not dados:
        return Response(
            {"detail": "Utente não encontrado."},
            status=status.HTTP_404_NOT_FOUND
        )

    dados_anonimizados = {
        "utente": anonimizar_utente_dict(dados["utente"]),
        "episodio_atual": dados["episodio_atual"],
        "episodios_passados": dados["episodios_passados"],
    }

    return Response(dados_anonimizados, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsRececionistaOuAdmin])
def exportar_monitorizacao_json(request, utente_id):
    """
    Exporta a monitorização administrativa em JSON.
    """
    dados = MonitorizacaoAdministrativaService.consultar_monitorizacao_utente(utente_id)

    if not dados:
        return Response(
            {"detail": "Utente não encontrado."},
            status=status.HTTP_404_NOT_FOUND
        )

    return Response(dados, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsRececionistaOuAdmin])
def exportar_monitorizacao_csv(request, utente_id):
    """
    Exporta dados administrativos básicos do utente em CSV.
    """
    dados = MonitorizacaoAdministrativaService.consultar_monitorizacao_utente(utente_id)

    if not dados:
        return Response(
            {"detail": "Utente não encontrado."},
            status=status.HTTP_404_NOT_FOUND
        )

    utente = dados["utente"]
    episodio_atual = dados["episodio_atual"] or {}

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = f'attachment; filename="utente_{utente_id}_monitorizacao.csv"'

    writer = csv.writer(response)
    writer.writerow([
        "nome",
        "numero_utente",
        "nif",
        "telefone",
        "medico_responsavel",
        "diagnostico",
        "estado_atual",
        "tempo_decorrido_minutos",
        "tempo_previsivel_alta",
    ])
    writer.writerow([
        utente.get("nome"),
        utente.get("numero_utente"),
        utente.get("nif"),
        utente.get("telefone"),
        episodio_atual.get("medico_responsavel"),
        episodio_atual.get("diagnostico"),
        episodio_atual.get("estado_atual"),
        episodio_atual.get("tempo_decorrido_minutos"),
        episodio_atual.get("tempo_previsivel_alta"),
    ])

    return response