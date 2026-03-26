# apps/internamentos/views.py

from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Internamento, ResumoDiarioInternamento
from .serializers import InternamentoSerializer, ResumoDiarioInternamentoSerializer
from .services import InternamentoService

from apps.common.permissions import IsProfissionalSaudeOuAdmin


class InternamentoViewSet(viewsets.ModelViewSet):
    """
    CRUD de internamentos.
    """

    queryset = Internamento.objects.all().order_by("-data_internamento")
    serializer_class = InternamentoSerializer
    permission_classes = [IsProfissionalSaudeOuAdmin]


class ResumoDiarioInternamentoViewSet(viewsets.ModelViewSet):
    """
    CRUD dos resumos diários do internamento.
    """

    queryset = ResumoDiarioInternamento.objects.all().order_by("-data_resumo")
    serializer_class = ResumoDiarioInternamentoSerializer
    permission_classes = [IsProfissionalSaudeOuAdmin]


@api_view(["GET"])
@permission_classes([IsProfissionalSaudeOuAdmin])
def consultar_utente_internado(request, utente_id):
    """
    Endpoint para consultar um utente internado com os dados principais
    pedidos no enunciado.
    """
    dados = InternamentoService.consultar_utente_internado(utente_id)

    if not dados:
        return Response(
            {"detail": "Utente internado não encontrado."},
            status=status.HTTP_404_NOT_FOUND
        )

    return Response(dados, status=status.HTTP_200_OK)