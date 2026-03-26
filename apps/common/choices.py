# apps/common/choices.py

SEXO_CHOICES = [
    ("M", "Masculino"),
    ("F", "Feminino"),
    ("O", "Outro"),
]

TRIAGEM_MANCHESTER_CHOICES = [
    ("VERMELHO", "Vermelho - Emergente"),
    ("LARANJA", "Laranja - Muito urgente"),
    ("AMARELO", "Amarelo - Urgente"),
    ("VERDE", "Verde - Pouco urgente"),
    ("AZUL", "Azul - Não urgente"),
]

ESTADO_EPISODIO_CHOICES = [
    ("AGUARDA_OBSERVACAO", "Aguarda Observação médica"),
    ("AGUARDA_EXAME", "Aguarda realização de exame"),
    ("AGUARDA_RESULTADO", "Aguarda resultado do exame"),
    ("AGUARDA_TERAPEUTICA", "Aguarda realização terapêutica"),
    ("AGUARDA_INTERNAMENTO", "Aguarda internamento"),
    ("INTERNADO", "Internado"),
    ("ALTA", "Alta"),
    ("ENCERRADO", "Encerrado"),
]

TIPO_PROFISSIONAL_CHOICES = [
    ("MEDICO", "Médico"),
    ("ENFERMEIRO", "Enfermeiro"),
    ("ADMINISTRATIVO", "Administrativo"),
    ("RECECIONISTA", "Rececionista"),
    ("ADMIN", "Administrador"),
]

TIPO_EXAME_CHOICES = [
    ("ANALISES", "Análises"),
    ("RX", "Raio-X"),
    ("TAC", "TAC"),
    ("RM", "Ressonância Magnética"),
    ("ECOGRAFIA", "Ecografia"),
    ("ECG", "Eletrocardiograma"),
    ("OUTRO", "Outro"),
]

ESTADO_EXAME_CHOICES = [
    ("PEDIDO", "Pedido"),
    ("EM_EXECUCAO", "Em execução"),
    ("CONCLUIDO", "Concluído"),
    ("RESULTADO_DISPONIVEL", "Resultado disponível"),
]

TIPO_FATURA_CHOICES = [
    ("EPISODIO_ATUAL", "Episódio Atual"),
    ("EPISODIO_PASSADO", "Episódio Passado"),
]

TIPO_CONSULTA_CHOICES = [
    ("OBSERVACAO_INICIAL", "Observação inicial"),
    ("REAVALIACAO", "Reavaliação"),
    ("CONSULTA_ESPECIALIDADE", "Consulta de especialidade"),
]

TIPO_PRESCRICAO_CHOICES = [
    ("MEDICACAO", "Medicação"),
    ("TERAPEUTICA", "Terapêutica"),
    ("ORIENTACAO", "Orientação clínica"),
]