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

        soap = BeautifulSoup(self.sourcecode)
        remove = soap.find_all(text=lambda text: isinstance(text, Comment))
        ispassou = True
        for removeitem in remove:  # remove o código html comentado
            removeitem.extract()
            Fieldsetcoll = soap.select('form fieldset')

        if not Fieldsetcoll:
            self.occurrences.add(OccurrenceInterface(self.rec, 1, "", 1))
            ispassou = False
        else:
            for item in Fieldsetcoll:
                if not item.findAll('legend'):
                    self.occurrences.add(OccurrenceInterface(self.rec, 2, item, 1))
                    ispassou = False

        for item in soap.select('select'):
            optgroupcoll = item.findAll('optgroup')
            if not optgroupcoll:
                self.occurrences.add(OccurrenceInterface(self.rec, 3, item, 1))
                ispassou = False
            else:
                for optgroup in optgroupcoll:
                    if not optgroup['label']:
                        self.occurrences.add(OccurrenceInterface(self.rec, 4, optgroup, 1))
                        ispassou = False

        if ispassou:
            self.occurrences.add(OccurrenceInterface(self.rec, 0, "", 1))

        return self.occurrences.list_of_occurrences