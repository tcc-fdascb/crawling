class OccurrenceInterface:
    """
    Modelo do objeto de Ocorrência

    @param: code - código da verifição
    @param: message - mensagem que descreve a verificação
    @param: tag - node html que foi verificado
    """

    def __init__(self, recommendation, code_feedback, code_message, tag):
        self.recommendation = recommendation
        self.code_feedback = code_feedback
        self.code_message = code_message
        self.tag = tag
