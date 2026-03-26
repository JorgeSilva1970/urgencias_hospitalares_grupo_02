# apps/internamentos/models.py

from django.db import models
from django.conf import settings
from apps.episodios.models import EpisodioUrgencia


class Internamento(models.Model):
    """
    Representa o internamento de um utente após episódio de urgência.
    """

    episodio = models.OneToOneField(
        EpisodioUrgencia,
        on_delete=models.CASCADE,
        related_name="internamento"
    )

    data_internamento = models.DateTimeField()
    data_alta_hospitalar = models.DateTimeField(null=True, blank=True)

    servico = models.CharField(max_length=100)
    cama = models.CharField(max_length=20)

    medico_responsavel = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="internamentos_como_medico"
    )

    enfermeiro_responsavel = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="internamentos_como_enfermeiro"
    )

    terapeutica_atual = models.TextField(blank=True, null=True)
    observacoes_transferencia = models.TextField(blank=True, null=True)

    @property
    def numero_dias_internado(self):
        from django.utils import timezone
        fim = self.data_alta_hospitalar or timezone.now()
        return (fim.date() - self.data_internamento.date()).days

    def __str__(self):
        return f"Internamento do episódio {self.episodio.id} - {self.servico} / {self.cama}"


class ResumoDiarioInternamento(models.Model):
    """
    Resumo diário do internamento.
    """

    internamento = models.ForeignKey(
        Internamento,
        on_delete=models.CASCADE,
        related_name="resumos_diarios"
    )

    data_resumo = models.DateField()
    resumo = models.TextField()

    class Meta:
        unique_together = ("internamento", "data_resumo")

    def __str__(self):
        return f"Resumo {self.data_resumo} - Internamento {self.internamento.id}"