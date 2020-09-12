from bs4 import BeautifulSoup , Comment

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface


class Recommendation07:
    """
    Recomendação 07: Não utilizar tabelas para diagramação
    """

    def __init__(self, sourcecode):
        self.rec = 7
        self.sourcecode = sourcecode
        self.occurrences = Occurrences()

    def avaliacao(self):


        soap = BeautifulSoup(self.sourcecode, 'html.parser')
        remove = soap.find_all(text=lambda text:isinstance(text, Comment))
        for removeitem in remove: #remove o código html comentado
            removeitem.extract()

        # tables = soap.select('table form')

        for tableitem in soap.select('table form'):
            if tableitem:
                self.occurrences.add(OccurrenceInterface(self.rec, 1, tableitem))


        for verifica in ['topo', 'main', 'rodape', 'principal', 'menu', 'nav', 'navigation', 'navegacao', 'header', 'footer']:
            selectionclass = 'table .' + verifica
            selectionids   = 'table #'+ verifica

            if soap.select(selectionclass ) or soap.select(selectionids):
                # erro