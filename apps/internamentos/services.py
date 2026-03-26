# apps/internamentos/services.py

from apps.internamentos.repositories import InternamentoRepository


class InternamentoService:
    """
    Camada de serviço para regras de negócio relacionadas com internamento.
    """

    @staticmethod
    def consultar_utente_internado(utente_id):
        """
        Devolve uma estrutura pronta para resposta da API com os dados
        pedidos no enunciado para consulta de utente internado.
        """
        internamento = InternamentoRepository.obter_internamento_por_utente_id(utente_id)

        if not internamento:
            return None

        resumo_hoje = InternamentoRepository.obter_resumo_de_hoje(internamento)
        ultimos_exames = InternamentoRepository.obter_ultimos_exames(internamento)

        dados = {
            "utente_id": internamento.episodio.utente.id,
            "nome_utente": internamento.episodio.utente.nome,
            "numero_utente": internamento.episodio.utente.numero_utente,

            "episodio_id": internamento.episodio.id,
            "data_internamento": internamento.data_internamento,
            "servico": internamento.servico,
            "cama": internamento.cama,

            "medico_responsavel": (
                internamento.medico_responsavel.username
                if internamento.medico_responsavel else None
            ),
            "enfermeiro_responsavel": (
                internamento.enfermeiro_responsavel.username
                if internamento.enfermeiro_responsavel else None
            ),

            "numero_dias_internado": internamento.numero_dias_internado,
            "terapeutica_atual": internamento.terapeutica_atual,
            "resumo_diario_hoje": resumo_hoje.resumo if resumo_hoje else None,

            "ultimos_exames": [
                {
                    "id": exame.id,
                    "tipo_exame": exame.tipo_exame,
                    "descricao": exame.descricao,
                    "estado": exame.estado,
                    "data_pedido": exame.data_pedido,
                    "data_resultado": exame.data_resultado,
                    "resultado": exame.resultado,
                }
                for exame in ultimos_exames
            ]
        }

        return dados