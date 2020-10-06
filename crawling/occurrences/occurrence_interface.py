class OccurrenceInterface:
    """
    Modelo do objeto de Ocorrência

    @param: recommendation - código da recomendação
    @param: code_message - código da mensagem
    @param: tag - tag HTML que foi avaliada
    """

    def __init__(self, recommendation, code_message, tag, peso):
        self.recommendation = recommendation
        self.code_message = code_message
        self.tag = tag
        #self.type_feedback = type_feedback
        self.peso = peso
