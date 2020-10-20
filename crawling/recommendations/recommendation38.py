from bs4 import BeautifulSoup

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface


class Recommendation38:
    """
    Recomendação 38: Fornecer alternativa em texto para os botões de imagem de formulários
    """

    def __init__(self, sourcecode):
        self.rec = 38
        self.sourcecode = sourcecode
        self.occurrences = Occurrences()

    def avaliacao(self):
        soap = BeautifulSoup(self.sourcecode, 'html.parser')

        inputs = soap.select('input')

        if len(inputs) > 0:
            for input_tag in inputs:
                ispassou = True
                attr_type = input_tag.get('type')

                if attr_type:
                    if attr_type == 'image':
                        if not input_tag.get('alt'):
                            ispassou = False
                            self.occurrences.add(OccurrenceInterface(self.rec, 1, input_tag, 3))

                    if attr_type == 'reset' or attr_type == 'button' or attr_type == 'submit':
                        if not input_tag.get('value'):
                            ispassou = False
                            self.occurrences.add(OccurrenceInterface(self.rec, 1, input_tag, 3))
                else:
                    ispassou = False
                    self.occurrences.add(OccurrenceInterface(self.rec, 2, input_tag, 3))

                if ispassou:
                    self.occurrences.add(OccurrenceInterface(self.rec, 0, input_tag, 3))

        return self.occurrences.list_of_occurrences
