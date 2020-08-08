from bs4 import BeautifulSoup

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface


class Recommendation20:
    """
    Recomendação 20: Fornecer alternativa em texto para as imagens do sítio
    Descrição da recomendação se houver
    """

    def __init__(self, sourcecode):
        self.sourcecode = sourcecode
        self.occurrences = Occurrences()

    def avaliacao(self):
        soap = BeautifulSoup(self.sourcecode, 'html.parser')
        imagens = soap.find_all('img')

        for imagem in imagens:
            if not imagem.has_attr('alt'):
                self.occurrences.add(OccurrenceInterface(2, 'Não possui o atributo "alt"', imagem))
            elif not imagem['alt']:
                self.occurrences.add(OccurrenceInterface(1, 'Não possui valor no atributo "alt"', imagem))
            else:
                self.occurrences.add(OccurrenceInterface(0, 'Possui valor no atributo "alt"', imagem))

        return self.occurrences.list_of_occurrences
