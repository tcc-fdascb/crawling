from bs4 import BeautifulSoup

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface


class recommendation33:
    """
    5.1 - Fornecer alternativa para vídeo
    5.2 - Fornecer alternativa para áudio
    5.3 - Oferecer audiodescrição para vídeo pré-gravado

    """

    def __init__(self, sourcecode):
        self.rec = 51
        self.sourcecode = sourcecode
        self.occurrences = Occurrences()

    def avaliacao(self):
        soap = BeautifulSoup(self.sourcecode, 'html.parser')
        videos = soap.find_all('video')

        for video in videos:
            self.occurrences.add(OccurrenceInterface(self.rec, 2, video))
        return self.occurrences.list_of_occurrences
