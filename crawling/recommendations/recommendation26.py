from bs4 import BeautifulSoup

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface


class Recommendation26:
    """
    Recomendação 26: Disponibilizar uma explicação para siglas, abreviaturas e palavras incomuns
    """

    def __init__(self, sourcecode):
        self.rec = 26
        self.occurrences = Occurrences()
        self.sourcecode = sourcecode

    def avaliacao(self):
        soap = BeautifulSoup(self.sourcecode, 'html.parser')
        abbrs = soap.find_all('abbr')

        if abbrs:
            for abbr in abbrs:
                if not abbr.get('title'):
                    self.occurrences.add(OccurrenceInterface(self.rec, 1, abbr, 1))
                else:
                    self.occurrences.add(OccurrenceInterface(self.rec, 0, abbr, 1))

        return self.occurrences.list_of_occurrences
