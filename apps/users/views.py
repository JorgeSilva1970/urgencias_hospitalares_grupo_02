# apps/users/views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer
from apps.common.permissions import IsAdmin


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Apenas leitura de utilizadores.
    Normalmente só o admin deve consultar a lista completa.
    """

    queryset = User.objects.all().order_by("username")
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]