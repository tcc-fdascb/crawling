class OccurrenceInterface:
    """
    Modelo do objeto de Ocorrência

    @param: recommendation - código da recomendação
    @param: feedback_type - tipo do feedback (0 - Ok, 1 - Erro ou 2 - Alerta)
    @param: code_message - código da mensagem
    """

    def __init__(self, recommendation, code_message, tag):
        self.recommendation = recommendation
        self.code_message = code_message
        self.tag = tag
