class OccurrenceInterface:
    """
    Modelo do objeto de Ocorrência

    @param: recommendation - código da recomendação
    @param: code_message - código da mensagem
    @param: tag - tag HTML que foi avaliada
    @param: peso - peso da recomendação
    """
    def __init__(self, recommendation, code_message, tag, peso):
        self.recommendation = recommendation
        self.code_message = code_message
        self.tag = tag
        self.peso = peso
