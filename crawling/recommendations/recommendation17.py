from bs4 import BeautifulSoup

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface


class Recommendation17:
    """
    Recomendação 17: Nome da recomendação
    - Título descritivo.
    """

    def __init__(self, sourcecode):
        self.rec = 17
        self.sourcecode = sourcecode
        self.occurrences = Occurrences()

    def avaliacao(self):
        soap = BeautifulSoup(self.sourcecode, 'html.parser')
        titles = soap.find_all('title')

        for title in titles:
            self.occurrences.add(OccurrenceInterface(self.rec, 2, title, 2))
        return self.occurrences.list_of_occurrences
