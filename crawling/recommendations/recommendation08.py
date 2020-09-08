from bs4 import BeautifulSoup , Comment

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface


class Recommendation08:
    """
    Recomendação 08: Separar links adjacentes
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


        print( soapfiltro.select('p > a ') )