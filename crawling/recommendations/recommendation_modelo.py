class RecommendationModelo:
    """
    Recomendação Modelo: Nome da recomendação
    Descrição da recomendação se houver

    :param name - Recebe o nome da Recomendação
    """

    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)
