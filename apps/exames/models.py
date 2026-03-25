# apps/exames/models.py

from django.db import models
from django.conf import settings
from apps.episodios.models import EpisodioUrgencia
from apps.common.choices import TIPO_EXAME_CHOICES, ESTADO_EXAME_CHOICES


class Exame(models.Model):
    """
    Exames pedidos e realizados no âmbito do episódio.
    """

    episodio = models.ForeignKey(
        EpisodioUrgencia,
        on_delete=models.CASCADE,
        related_name="exames"
    )

    tipo_exame = models.CharField(max_length=20, choices=TIPO_EXAME_CHOICES)
    descricao = models.TextField()

    medico_pedido = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="exames_pedidos"
    )

    data_pedido = models.DateTimeField()
    data_realizacao = models.DateTimeField(null=True, blank=True)
    data_resultado = models.DateTimeField(null=True, blank=True)

    estado = models.CharField(
        max_length=25,
        choices=ESTADO_EXAME_CHOICES,
        default="PEDIDO"
    )

    resultado = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.tipo_exame} - Episódio {self.episodio.id}"