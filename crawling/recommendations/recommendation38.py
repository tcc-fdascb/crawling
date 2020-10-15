from bs4 import BeautifulSoup , Comment

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
        remove = soap.find_all(text=lambda text:isinstance(text, Comment))

        ispassou = True
        # remove o código html comentado
        for removeitem in remove:
            removeitem.extract()
        soapfiltro = BeautifulSoup(soap.prettify(), 'html.parser')

        for inputverifica in soapfiltro.select('input'):
             if inputverifica['type'] == 'image':
                 if not inputverifica['alt']:
                    self.occurrences.add(OccurrenceInterface(self.rec, 1, inputverifica, 3))
                    ispassou = False

             if inputverifica['type'] == 'reset':
                 if not inputverifica['value']:
                    self.occurrences.add(OccurrenceInterface(self.rec, 1, inputverifica, 3))
                    ispassou = False

             if inputverifica['type'] == 'button':
                 if not inputverifica['value']:
                    self.occurrences.add(OccurrenceInterface(self.rec, 1, inputverifica, 3))
                    ispassou = False

             if inputverifica['type'] == 'submit':
                 if not inputverifica['value']:
                    self.occurrences.add(OccurrenceInterface(self.rec, 1, inputverifica, 3))
                    ispassou = False

        if ispassou:
            self.occurrences.add(OccurrenceInterface(self.rec, 0, "", 3))

        return self.occurrences.list_of_occurrences