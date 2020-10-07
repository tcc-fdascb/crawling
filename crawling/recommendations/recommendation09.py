from bs4 import BeautifulSoup

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface


class Recommendation09:
    """
    Recomendação 9: Não abrir novas instâncias sem a solicitação do usuário
    """

    def __init__(self, sourcecode):
        self.rec = 9
        self.sourcecode = sourcecode
        self.occurrences = Occurrences()

    def avaliacao(self):
        soap = BeautifulSoup(self.sourcecode, 'html.parser')
        targets = soap.find_all('a')

        for target in targets:
            if target.has_attr('target'):
                self.occurrences.add(OccurrenceInterface(self.rec, 1, target, 2))
            else:
                self.occurrences.add(OccurrenceInterface(self.rec, 0, target, 2))
        return self.occurrences.list_of_occurrences
