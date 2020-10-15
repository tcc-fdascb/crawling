from bs4 import BeautifulSoup, Comment

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface

class Recommendation03:
    """
        Recomendação 03: Utilizar corretamente os níveis de cabeçalho

    """
    def __init__(self, sourcecode):
        self.rec = 3
        self.sourcecode = sourcecode
        self.occurrences = Occurrences()

    def avaliacao(self):
        ispassou = True
        soap = BeautifulSoup(self.sourcecode, 'html.parser')

        if soap.findAll('h1'):
            self.occurrences.add(OccurrenceInterface(self.rec, 1, "", 2))
            ispassou = False


        if ispassou:
            self.occurrences.add(OccurrenceInterface(self.rec, 0, "", 2))

        return self.occurrences.list_of_occurrences