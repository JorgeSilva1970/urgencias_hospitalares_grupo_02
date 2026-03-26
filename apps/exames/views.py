# apps/exames/views.py

from rest_framework import viewsets
from .models import Exame
from .serializers import ExameSerializer
from apps.common.permissions import IsProfissionalSaudeOuAdmin


class ExameViewSet(viewsets.ModelViewSet):
    """
    CRUD de exames.
    """

    queryset = Exame.objects.all().order_by("-data_pedido")
    serializer_class = ExameSerializer
    permission_classes = [IsProfissionalSaudeOuAdmin]

    def get_queryset(self):
        """
        Filtro por episódio e por estado do exame.
        """
        queryset = super().get_queryset()
        episodio = self.request.query_params.get("episodio")
        estado = self.request.query_params.get("estado")

        if episodio:
            queryset = queryset.filter(episodio_id=episodio)

        if estado:
            queryset = queryset.filter(estado=estado)

        return queryset