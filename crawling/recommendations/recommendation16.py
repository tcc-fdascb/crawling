from bs4 import BeautifulSoup

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface


class Recommendation16:
    """
    Recomendação 16 – Identificar o idioma principal da página
    """

    def __init__(self, sourcecode):
        self.rec = 16
        self.sourcecode = sourcecode
        self.occurrences = Occurrences()

    def avaliacao(self):
        soap = BeautifulSoup(self.sourcecode, 'html.parser')
        lang = soap.find("html").get('lang')

        if lang == 'pt-br':
            self.occurrences.add(OccurrenceInterface(self.rec, 0, lang, 2))
        elif lang == 'pt-BR':
            self.occurrences.add(OccurrenceInterface(self.rec, 0, lang, 2))
        elif lang == 'PT-BR':
            self.occurrences.add(OccurrenceInterface(self.rec, 0, lang, 2))
        else:
            self.occurrences.add(OccurrenceInterface(self.rec, 1, lang, 2))

        return self.occurrences.list_of_occurrences
