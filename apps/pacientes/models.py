# apps/pacientes/models.py

from django.db import models
from apps.common.choices import SEXO_CHOICES


class Utente(models.Model):
    """
    Representa um utente do hospital.
    Inclui os dados administrativos pedidos no enunciado.
    """

    numero_utente = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=150)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)

    nif = models.CharField(max_length=9, unique=True)
    morada = models.CharField(max_length=255)
    codigo_postal = models.CharField(max_length=12)
    telefone = models.CharField(max_length=20)

    contacto_terceiro_nome = models.CharField(max_length=150)
    contacto_terceiro_telefone = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.numero_utente} - {self.nome}"