from bs4 import BeautifulSoup

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface

class Recommendation19:
    """
    Recomendação 19: Nome da recomendação
    - Descrição de Links.
    """

    def __init__(self, sourcecode):
        self.rec = 19
        self.sourcecode = sourcecode
        self.occurrences = Occurrences()

    def avaliacao(self):
        soap = BeautifulSoup(self.sourcecode, 'html.parser')

        for link in soap.find_all('a'):
            links = (link.get('href'))
            self.occurrences.add(OccurrenceInterface(self.rec, 2, links, 2))
        return self.occurrences.list_of_occurrences
