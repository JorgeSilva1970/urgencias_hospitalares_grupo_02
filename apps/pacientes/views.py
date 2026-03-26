# apps/pacientes/views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Utente
from .serializers import UtenteSerializer


class UtenteViewSet(viewsets.ModelViewSet):
    """
    CRUD completo de utentes.
    """

    queryset = Utente.objects.all().order_by("nome")
    serializer_class = UtenteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Permite pesquisa simples por nome, número de utente ou NIF.
        Exemplo:
        /api/pacientes/utentes/?search=maria
        """
        queryset = super().get_queryset()
        search = self.request.query_params.get("search")

        if search:
            queryset = queryset.filter(nome__icontains=search) | \
                       queryset.filter(numero_utente__icontains=search) | \
                       queryset.filter(nif__icontains=search)

        return queryset
