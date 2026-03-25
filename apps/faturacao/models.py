# apps/faturacao/models.py

from django.db import models
from apps.episodios.models import EpisodioUrgencia
from apps.common.choices import TIPO_FATURA_CHOICES


class Faturacao(models.Model):
    """
    Registo de faturação associado ao episódio.
    """

    episodio = models.ForeignKey(
        EpisodioUrgencia,
        on_delete=models.CASCADE,
        related_name="faturacoes"
    )

    tipo = models.CharField(max_length=20, choices=TIPO_FATURA_CHOICES)
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_registo = models.DateTimeField(auto_now_add=True)
    pago = models.BooleanField(default=False)

    def __str__(self):
        return f"Faturação {self.episodio.id} - {self.valor}€"
