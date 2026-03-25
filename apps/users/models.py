# apps/users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.common.choices import TIPO_PROFISSIONAL_CHOICES


class User(AbstractUser):
    """
    Utilizador do sistema.
    Foi estendido para suportar o papel/perfil no hospital.
    """

    tipo_profissional = models.CharField(
        max_length=20,
        choices=TIPO_PROFISSIONAL_CHOICES,
        default="ADMINISTRATIVO"
    )

    numero_mecanografico = models.CharField(
        max_length=20,
        unique=True,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.username} - {self.tipo_profissional}"