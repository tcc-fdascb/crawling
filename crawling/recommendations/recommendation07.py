from bs4 import BeautifulSoup , Comment

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface


class Recommendation07:
    """
    Recomendação 07: Não utilizar tabelas para diagramação
    """

    def __init__(self, sourcecode):
        self.rec = 07
        self.sourcecode = sourcecode
        self.occurrences = Occurrences()

    def avaliacao(self):


        soap = BeautifulSoup(self.sourcecode, 'html.parser')
        remove = soap.find_all(text=lambda text:isinstance(text, Comment))
        for removeitem in remove: #remove o código html comentado
            removeitem.extract()

        tables = remove.select('table')

        for tableitem in tables:
            if ["colspan","border","cellpadding","frame"] in tableitem.attrs:
                self.occurrences.add(OccurrenceInterface(self.rec, 1, 1, tableitem))
            if verificaformulario in remove.select('tr > input'):

            if verificaformulario in remove.select('th > input'):