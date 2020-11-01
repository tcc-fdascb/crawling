from bs4 import BeautifulSoup

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface


class Recommendation17:
    """
    Recomendação 17: Oferecer um título descritivo e informativo à página
    """

    def __init__(self, sourcecode):
        self.rec = 17
        self.sourcecode = sourcecode
        self.occurrences = Occurrences()

    def avaliacao(self):
        soap = BeautifulSoup(self.sourcecode, 'html.parser')
        titles = soap.find_all('title')

        if titles:
            if len(titles) > 1:
                self.occurrences.add(OccurrenceInterface(self.rec, 2, titles, 2))
            else:
                self.occurrences.add(OccurrenceInterface(self.rec, 0, titles[0], 2))
        else:
            self.occurrences.add(OccurrenceInterface(self.rec, 1, '', 2))
        return self.occurrences.list_of_occurrences
