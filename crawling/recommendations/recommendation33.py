from bs4 import BeautifulSoup

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface


class Recommendation33:
    """
    Recomendação 33: Nome da recomendação
    - Fornecer alternativa para vídeo
    - Fornecer alternativa para áudio
    - Oferecer audiodescrição para vídeo pré-gravado
    """

    def __init__(self, sourcecode):
        self.rec = 33
        self.sourcecode = sourcecode
        self.occurrences = Occurrences()

    def avaliacao(self):
        soap = BeautifulSoup(self.sourcecode, 'html.parser')
        videos = soap.find_all('video')

        for video in videos:
            self.occurrences.add(OccurrenceInterface(self.rec, 2, video, 3))
        return self.occurrences.list_of_occurrences
