from bs4 import BeautifulSoup

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
        tables = soap.select('table')

        for table in tables:
            ispassou = True
            words = ['topo', 'main', 'rodape', 'principal', 'menu', 'nav',
                     'navigation', 'navegacao', 'header', 'footer']

            if table.get('id'):
                check = any(item in table.get('id') for item in words)
                if check:
                    self.occurrences.add(OccurrenceInterface(self.rec, 1, table, 2))
                    ispassou = False

            if table.get('class'):
                check = any(item in table.get('class') for item in words)
                if check:
                    self.occurrences.add(OccurrenceInterface(self.rec, 1, table, 2))
                    ispassou = False

            for word in words:
                childclass = table.select('.' + word)
                childid = table.select('#' + word)

                if childclass:
                    self.occurrences.add(OccurrenceInterface(self.rec, 1, childclass, 2))
                    ispassou = False

                if childid:
                    self.occurrences.add(OccurrenceInterface(self.rec, 1, childclass, 2))
                    ispassou = False

            if len(table.select('form')) > 0:
                self.occurrences.add(OccurrenceInterface(self.rec, 2, table, 2))
                ispassou = False

            if ispassou:
                pass
                self.occurrences.add(OccurrenceInterface(self.rec, 0, "", 2))

        if len(soap.select('body > iframe')) > 0 and\
                len(soap.select('body > div')) == 0 and\
                len(soap.select('body > main')) == 0:
            self.occurrences.add(OccurrenceInterface(self.rec, 3, "", 2))

        return self.occurrences.list_of_occurrences
