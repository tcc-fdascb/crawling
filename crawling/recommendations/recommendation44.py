from bs4 import BeautifulSoup, Comment

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface

class Recommendation44:
    """
        Recomendação 44: Utilizar corretamente os níveis de cabeçalho

    """
    def __init__(self, sourcecode):
        self.rec = 44
        self.sourcecode = sourcecode
        self.occurrences = Occurrences()

    def avaliacao(self):
        ispassou = True
        soap = BeautifulSoup(self.sourcecode)
        remove = soap.find_all(text=lambda text: isinstance(text, Comment))
        ispassou = True
        for removeitem in remove:  # remove o código html comentado
            removeitem.extract()
        if not soap.select('form fieldset'):
            self.occurrences.add(OccurrenceInterface(self.rec, 1, "", 2))
            ispassou = False


        if ispassou:
            self.occurrences.add(OccurrenceInterface(self.rec, 0, "", 2))

        return self.occurrences.list_of_occurrences