# apps/episodios/services.py

from django.db import transaction
from .models import EpisodioUrgencia, Triagem


class EpisodioService:
    """
    Serviço para operações transacionais do módulo de episódios.
    """

    @staticmethod
    @transaction.atomic
    def criar_episodio_com_triagem(dados_episodio, dados_triagem):
        """
        Cria episódio e triagem na mesma transação.
        Se algo falhar, nada fica gravado parcialmente.
        """
        episodio = EpisodioUrgencia.objects.create(**dados_episodio)
        Triagem.objects.create(episodio=episodio, **dados_triagem)
        return episodio