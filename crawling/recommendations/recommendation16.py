from bs4 import BeautifulSoup

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface


class recommendation16:
    """
    Recomendação 3.1 – Identificar o idioma principal da página
    """

    def __init__(self, sourcecode):
        self.rec = 31
        self.sourcecode = sourcecode
        self.occurrences = Occurrences()

    def avaliacao(self):
        soap = BeautifulSoup(self.sourcecode, 'html.parser')
        lang = soap.find("html").get('lang')

        if lang == 'pt-br':
<<<<<<< HEAD:crawling/recommendations/recommendation16.py
            self.occurrences.add(OccurrenceInterface(self.rec, 0, lang, 2))
        elif lang == 'pt-BR':
            self.occurrences.add(OccurrenceInterface(self.rec, 0, lang, 2))
        elif lang == 'PT-BR':
            self.occurrences.add(OccurrenceInterface(self.rec, 0, lang, 2))
        else:
            self.occurrences.add(OccurrenceInterface(self.rec, 1, lang, 2))
=======
            self.occurrences.add(OccurrenceInterface(self.rec, 0, lang))
        elif lang == 'pt-BR':
            self.occurrences.add(OccurrenceInterface(self.rec, 0, lang))
        elif lang == 'PT-BR':
            self.occurrences.add(OccurrenceInterface(self.rec, 0, lang))
        else:
            self.occurrences.add(OccurrenceInterface(self.rec, 1, lang))
>>>>>>> c6735115ecb9c956c4abbc4292e39199d286cd75:crawling/recommendations/RecommendationEmag31.py
        return self.occurrences.list_of_occurrences
