from bs4 import BeautifulSoup

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface


class Recommendation31:
    """
    Recomendação 31: Nome da recomendação
    - Dividir as áreas de informação
    """

    def __init__(self, sourcecode):
        self.rec = 31
        self.sourcecode = sourcecode
        self.occurrences = Occurrences()
        self.lista_div = []

    def avaliacao(self):
        soap = BeautifulSoup(self.sourcecode, 'html.parser')
        lista = soap.find_all('div')
        x = self.lista_div.append(lista)

        return self.occurrences.add(OccurrenceInterface(self.rec, 2, len(x), 3))
