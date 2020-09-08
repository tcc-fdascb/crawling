from bs4 import BeautifulSoup , Comment

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface


class Recommendation38:
    """
    Recomendação 08: Fornecer alternativa em texto para os botões de imagem de formulários
    """

    def __init__(self, sourcecode):
        self.rec = 8
        self.sourcecode = sourcecode
        self.occurrences = Occurrences()

    def avaliacao(self):


        soap = BeautifulSoup(self.sourcecode, 'html.parser')
        remove = soap.find_all(text=lambda text:isinstance(text, Comment))
        for removeitem in remove: #remove o código html comentado
            removeitem.extract()
        soapfiltro = BeautifulSoup(soap.prettify(), 'html.parser')

        for inputverifica in soapfiltro.select('input'):
             if inputverifica['type'] == 'image':
                 if inputverifica['alt'] == '':
                     # erro
             if inputverifica['type'] == 'reset':
                 if inputverifica['value'] == '':

             if inputverifica['type'] == 'button':
                 if inputverifica['value'] == '':

             if inputverifica['type'] == 'submit':
                 if inputverifica['value'] == '':

        