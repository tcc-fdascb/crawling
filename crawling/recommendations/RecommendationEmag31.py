from bs4 import BeautifulSoup

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface


class RecommendationEmag31:
    """
    Recomendação 3.1 – Identificar o idioma principal da página
    """

    def __init__(self, sourcecode):
        self.rec = 31
        self.sourcecode = sourcecode
        self.occurrences = Occurrences()

    def avaliacao(self):
        soap = BeautifulSoup(self.sourcecode, 'html.parser')
        html = soap.decode('utf-8')
        lang = html.split()



        if'lang="pt-br"'in lang:
            pos = lang.index('lang="pt-br"')
            out = lang[pos]
            self.occurrences.add(OccurrenceInterface(self.rec, 0, out))
        else:
            self.occurrences.add(OccurrenceInterface(self.rec, 1, lang))
        return self.occurrences.list_of_occurrences