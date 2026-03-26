# apps/faturacao/services.py

from apps.faturacao.repositories import MonitorizacaoAdministrativaRepository


class MonitorizacaoAdministrativaService:
    """
    Camada de serviço da monitorização administrativa.
    """

    @staticmethod
    def consultar_monitorizacao_utente(utente_id):
        utente = MonitorizacaoAdministrativaRepository.obter_utente(utente_id)

        if not utente:
            return None

        episodio_atual = MonitorizacaoAdministrativaRepository.obter_episodio_atual(utente_id)
        episodios_passados = MonitorizacaoAdministrativaRepository.obter_episodios_passados(utente_id)

        dados = {
            "utente": {
                "id": utente.id,
                "nome": utente.nome,
                "numero_utente": utente.numero_utente,
                "nif": utente.nif,
                "morada": utente.morada,
                "codigo_postal": utente.codigo_postal,
                "telefone": utente.telefone,
                "contacto_terceiro_nome": utente.contacto_terceiro_nome,
                "contacto_terceiro_telefone": utente.contacto_terceiro_telefone,
            },
            "episodio_atual": None,
            "episodios_passados": [],
        }

        if episodio_atual:
            faturacao_atual = MonitorizacaoAdministrativaRepository.obter_faturacao_por_episodio(
                episodio_atual.id
            )

            dados["episodio_atual"] = {
                "id": episodio_atual.id,
                "data_hora_entrada": episodio_atual.data_hora_entrada,
                "data_hora_saida": episodio_atual.data_hora_saida,
                "hospital": episodio_atual.hospital.nome if episodio_atual.hospital else None,
                "medico_responsavel": (
                    episodio_atual.medico_responsavel.username
                    if episodio_atual.medico_responsavel else None
                ),
                "diagnostico": episodio_atual.diagnostico,
                "estado_atual": episodio_atual.estado_atual,
                "tempo_decorrido_minutos": episodio_atual.tempo_decorrido_minutos,
                "tempo_previsivel_alta": episodio_atual.tempo_previsivel_alta,
                "faturacao": [
                    {
                        "id": f.id,
                        "tipo": f.tipo,
                        "descricao": f.descricao,
                        "valor": str(f.valor),
                        "data_registo": f.data_registo,
                        "pago": f.pago,
                    }
                    for f in faturacao_atual
                ],
            }

        for episodio in episodios_passados:
            faturacao_passada = MonitorizacaoAdministrativaRepository.obter_faturacao_por_episodio(
                episodio.id
            )

            dados["episodios_passados"].append({
                "id": episodio.id,
                "data_hora_entrada": episodio.data_hora_entrada,
                "data_hora_saida": episodio.data_hora_saida,
                "hospital": episodio.hospital.nome if episodio.hospital else None,
                "medico_responsavel": (
                    episodio.medico_responsavel.username
                    if episodio.medico_responsavel else None
                ),
                "diagnostico": episodio.diagnostico,
                "estado_atual": episodio.estado_atual,
                "faturacao": [
                    {
                        "id": f.id,
                        "tipo": f.tipo,
                        "descricao": f.descricao,
                        "valor": str(f.valor),
                        "data_registo": f.data_registo,
                        "pago": f.pago,
                    }
                    for f in faturacao_passada
                ],
            })

        return dados