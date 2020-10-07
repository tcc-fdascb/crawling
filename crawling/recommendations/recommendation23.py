from bs4 import BeautifulSoup

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface


class Recommendation23:
    """
    Recomendação 23 – Em tabelas, utilizar títulos e resumos de forma apropriada
    """

    def __init__(self, sourcecode):
        self.rec = 23
        self.sourcecode = sourcecode
        self.occurrences = Occurrences()

    def avaliacao(self):
        soap = BeautifulSoup(self.sourcecode, 'html.parser')
        captions = soap.find_all('caption')

        for caption in captions:
            if caption.find_parents("table"):
                self.occurrences.add(OccurrenceInterface(self.rec, 0, caption, 3))
            else:
                self.occurrences.add(OccurrenceInterface(self.rec, 1, caption, 3))
        return self.occurrences.list_of_occurrences
