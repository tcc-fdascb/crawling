from bs4 import BeautifulSoup
import re

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface


class Recommendation08:
    """
    Recomendação 08: Separar links adjacentes
    """

    def __init__(self, sourcecode):
        self.rec = 8
        self.sourcecode = sourcecode
        self.occurrences = Occurrences()

    def avaliacao(self):
        soap = BeautifulSoup(self.sourcecode, 'html.parser')

        for paragraph in soap.find_all('p'):

            if len(paragraph.find_all('a')) > 0:
                par = str(paragraph).lower()
                par = re.sub('\n', '', par)
                par_sem_espaco = re.sub(' ', '', par)

                if '</a><a' in par_sem_espaco or \
                        '</a><br><a' in par_sem_espaco or \
                        '</a><br/><a' in par_sem_espaco:
                    self.occurrences.add(OccurrenceInterface(self.rec, 1, par, 2))
                else:
                    self.occurrences.add(OccurrenceInterface(self.rec, 0, par, 2))

        return self.occurrences.list_of_occurrences
