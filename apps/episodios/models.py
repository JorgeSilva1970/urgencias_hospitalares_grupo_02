# apps/episodios/models.py

from django.db import models
from django.conf import settings
from apps.pacientes.models import Utente
from apps.common.choices import (
    TRIAGEM_MANCHESTER_CHOICES,
    ESTADO_EPISODIO_CHOICES,
    TIPO_CONSULTA_CHOICES,
    TIPO_PRESCRICAO_CHOICES,
)


class Hospital(models.Model):
    """
    Hospital ou unidade hospitalar.
    """

    nome = models.CharField(max_length=150, unique=True)
    localizacao = models.CharField(max_length=150)

    def __str__(self):
        return self.nome


class EpisodioUrgencia(models.Model):
    """
    Episódio principal do utente na urgência.
    """

    utente = models.ForeignKey(
        Utente,
        on_delete=models.CASCADE,
        related_name="episodios"
    )

    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.PROTECT,
        related_name="episodios"
    )

    data_hora_entrada = models.DateTimeField()
    data_hora_saida = models.DateTimeField(null=True, blank=True)

    motivo_admissao = models.TextField()
    observacoes = models.TextField(blank=True, null=True)

    prioridade_manchester = models.CharField(
        max_length=20,
        choices=TRIAGEM_MANCHESTER_CHOICES
    )

    estado_atual = models.CharField(
        max_length=30,
        choices=ESTADO_EPISODIO_CHOICES,
        default="AGUARDA_OBSERVACAO"
    )

    medico_responsavel = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="episodios_como_medico"
    )

    enfermeiro_responsavel = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="episodios_como_enfermeiro"
    )

    diagnostico = models.TextField(blank=True, null=True)
    tempo_previsivel_alta = models.DateTimeField(null=True, blank=True)

    fechado = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def tempo_decorrido_minutos(self):
        from django.utils import timezone
        fim = self.data_hora_saida or timezone.now()
        diferenca = fim - self.data_hora_entrada
        return int(diferenca.total_seconds() // 60)

    def __str__(self):
        return f"Episódio {self.id} - {self.utente.nome}"


class Triagem(models.Model):
    """
    Registo da triagem do episódio.
    """

    episodio = models.OneToOneField(
        EpisodioUrgencia,
        on_delete=models.CASCADE,
        related_name="triagem"
    )

    enfermeiro = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="triagens_realizadas"
    )

    data_hora_triagem = models.DateTimeField()
    cor_manchester = models.CharField(
        max_length=20,
        choices=TRIAGEM_MANCHESTER_CHOICES
    )

    sintomas = models.TextField()
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Triagem {self.episodio.id} - {self.cor_manchester}"


class Consulta(models.Model):
    """
    Consulta/observação clínica no âmbito do episódio.
    """

    episodio = models.ForeignKey(
        EpisodioUrgencia,
        on_delete=models.CASCADE,
        related_name="consultas"
    )

    medico = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="consultas_realizadas"
    )

    data_hora = models.DateTimeField()
    tipo_consulta = models.CharField(
        max_length=30,
        choices=TIPO_CONSULTA_CHOICES
    )

    resumo_clinico = models.TextField()
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Consulta {self.id} - Episódio {self.episodio.id}"


class Prescricao(models.Model):
    """
    Prescrição associada ao episódio.
    """

    episodio = models.ForeignKey(
        EpisodioUrgencia,
        on_delete=models.CASCADE,
        related_name="prescricoes"
    )

    medico = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="prescricoes_emitidas"
    )

    data_hora = models.DateTimeField()
    tipo_prescricao = models.CharField(
        max_length=20,
        choices=TIPO_PRESCRICAO_CHOICES
    )

    descricao = models.TextField()
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return f"Prescrição {self.id} - Episódio {self.episodio.id}"