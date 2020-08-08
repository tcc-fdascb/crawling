class OccurrenceInterface:
    """
    Modelo do objeto de Ocorrência

    @param: code - código da verifição
    @param: message - mensagem que descreve a verificação
    @param: tag - node html que foi verificado
    """

    def __init__(self, code, message, tag):
        self.code = code
        self.message = message
        self.tag = tag
