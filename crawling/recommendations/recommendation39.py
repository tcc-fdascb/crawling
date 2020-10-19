from bs4 import BeautifulSoup , Comment

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface


class Recommendation39:
    """
    Recomendação 39: Associar etiquetas aos seus campos
    """

    def __init__(self, sourcecode):
        self.rec = 39
        self.sourcecode = sourcecode
        self.occurrences = Occurrences()

    def avaliacao(self):
        soap = BeautifulSoup(self.sourcecode, 'html.parser')
        ispassou = True
        labelscoll = soap.findAll('label')
        inputscoll = soap.findAll('input')
        selectscoll = soap.findAll('select')
        textareacoll = soap.findAll('textarea')

        for label in labelscoll:
            idlabel = str(label['id']).lower().strip()
            if not inputscoll:
                for item in inputscoll:
                    id = str(item['id']).lower().strip()
                    if id != idlabel:
                        self.occurrences.add(OccurrenceInterface(self.rec, 1, item, 3))
                        ispassou = False

            if not selectscoll:
                for item in selectscoll:
                    id = str(item['id']).lower().strip()
                    if id != idlabel:
                        self.occurrences.add(OccurrenceInterface(self.rec, 1, item, 3))
                        ispassou = False

            if not textareacoll:
                for item in textareacoll:
                    id = str(item['id']).lower().strip()
                    if id != idlabel:
                        self.occurrences.add(OccurrenceInterface(self.rec, 1, item, 3))
                        ispassou = False
        if ispassou:
            self.occurrences.add(OccurrenceInterface(self.rec, 0, "", 3))

        return self.occurrences.list_of_occurrences