from bs4 import BeautifulSoup
from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface

class Recommendation26:
    """
    Recomendação 26: Disponibilizar uma explicação para siglas,
                     abreviaturas e palavras incomuns

    """

    def __init__(self, sourcecode):
        self.rec = 26
        self.occurrences = Occurrences()
        self.sourcecode = sourcecode

    def print_name(self):
        print(self.name)

    def avaliacao(self):
        soap = BeautifulSoup(self.sourcecode, 'html.parser')
        verifyabbr = soap.select('abbr')
        ispassou = True
        if verifyabbr:
            for item in verifyabbr:
                if not item['title']:
                    ispassou = False
                    self.occurrences.add(OccurrenceInterface(self.rec, 1, item, 1))

        if ispassou:
            self.occurrences.add(OccurrenceInterface(self.rec, 0, "", 1))


        return self.occurrences.list_of_occurrences
