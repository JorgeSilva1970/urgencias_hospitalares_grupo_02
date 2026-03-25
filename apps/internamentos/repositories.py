# apps/internamentos/repositories.py

from django.utils import timezone
from apps.internamentos.models import Internamento
from apps.exames.models import Exame


class InternamentoRepository:
    """
    Repositório para centralizar consultas relacionadas com internamentos.
    """

    @staticmethod
    def obter_internamento_por_utente_id(utente_id):
        """
        Obtém o internamento ativo mais recente de um utente.
        """
        return (
            Internamento.objects
            .select_related(
                "episodio",
                "episodio__utente",
                "medico_responsavel",
                "enfermeiro_responsavel"
            )
            .filter(
                episodio__utente_id=utente_id
            )
            .order_by("-data_internamento")
            .first()
        )

    @staticmethod
    def obter_resumo_de_hoje(internamento):
        """
        Obtém o resumo diário do dia atual, se existir.
        """
        hoje = timezone.localdate()
        return internamento.resumos_diarios.filter(data_resumo=hoje).first()

    @staticmethod
    def obter_ultimos_exames(internamento, limite=5):
        """
        Obtém os últimos exames associados ao episódio do internamento.
        """
        return (
            Exame.objects
            .filter(episodio=internamento.episodio)
            .order_by("-data_pedido")[:limite]
        )