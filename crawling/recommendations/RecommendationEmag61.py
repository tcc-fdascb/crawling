from bs4 import BeautifulSoup

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface


class RecommendationEmag61:
    """
    6.1 – Fornecer alternativa em texto para os botões de imagem de formulários
    """

    def __init__(self, sourcecode):
        self.rec = 61
        self.sourcecode = sourcecode
        self.occurrences = Occurrences()

    def avaliacao(self):
        soap = BeautifulSoup(self.sourcecode, 'html.parser')
        linksa = soap.find_all('input')

        for links in linksa:
            if links.has_attr('alt'):
                self.occurrences.add(OccurrenceInterface(self.rec, 0, links))
            else:
                self.occurrences.add(OccurrenceInterface(self.rec, 1, links))
        return self.occurrences.list_of_occurrences
