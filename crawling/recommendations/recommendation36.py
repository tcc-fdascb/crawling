from bs4 import BeautifulSoup

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface


class Recommendation36:
    """
    Recomendação 36: Nome da recomendação
    - Fornecer controle para áudio
    """

    def __init__(self, sourcecode):
        self.rec = 36
        self.sourcecode = sourcecode
        self.occurrences = Occurrences()

    def avaliacao(self):
        soap = BeautifulSoup(self.sourcecode, 'html.parser')
        audios = soap.find_all('audio')

        for audios in audios:
            self.occurrences.add(OccurrenceInterface(self.rec, 2, audios, 2))
        return self.occurrences.list_of_occurrences
