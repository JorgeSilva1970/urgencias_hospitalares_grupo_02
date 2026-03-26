# apps/faturacao/repositories.py

from apps.pacientes.models import Utente
from apps.episodios.models import EpisodioUrgencia
from apps.faturacao.models import Faturacao


class MonitorizacaoAdministrativaRepository:
    """
    Repositório para consultas da área administrativa.
    """

    @staticmethod
    def obter_utente(utente_id):
        return Utente.objects.filter(id=utente_id).first()

    @staticmethod
    def obter_episodio_atual(utente_id):
        return (
            EpisodioUrgencia.objects
            .select_related("medico_responsavel", "enfermeiro_responsavel", "hospital")
            .filter(utente_id=utente_id, fechado=False)
            .order_by("-data_hora_entrada")
            .first()
        )

    @staticmethod
    def obter_episodios_passados(utente_id):
        return (
            EpisodioUrgencia.objects
            .select_related("medico_responsavel", "hospital")
            .filter(utente_id=utente_id, fechado=True)
            .order_by("-data_hora_entrada")
        )

    @staticmethod
    def obter_faturacao_por_episodio(episodio_id):
        return (
            Faturacao.objects
            .filter(episodio_id=episodio_id)
            .order_by("-data_registo")
        )