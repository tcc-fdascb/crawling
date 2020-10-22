from bs4 import BeautifulSoup

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface


class Recommendation24:
    """
    Recomendação 24: Associar células de dados às células de cabeçalho
    """

    def __init__(self, sourcecode):
        self.rec = 24
        self.occurrences = Occurrences()
        self.sourcecode = sourcecode

    def avaliacao(self):
        soap = BeautifulSoup(self.sourcecode, 'html.parser')
        tables = soap.find_all('table')

        for table in tables:
            ispassou = True
            th_cels = table.find_all('th')
            td_cels = table.find_all('td')
            th_cels_ids = []
            td_cels_headers = []
            th_cels_scope = []

            for th_cel in th_cels:
                if th_cel.get('id') is not None:
                    th_cels_ids.append(th_cel.get('id'))

            for td_cel in td_cels:
                temp = []
                if td_cel.get('headers') is not None:
                    temp.append(td_cel.get('headers'))
                    for header in temp:
                        for i in header:
                            td_cels_headers.append(i)

            for th_cel in th_cels:
                if th_cel.get('scope') is not None:
                    th_cels_scope.append(th_cel.get('scope'))

            if th_cels_ids and td_cels_headers:
                if not all(i in th_cels_ids for i in td_cels_headers):
                    ispassou = False
                    self.occurrences.add(OccurrenceInterface(self.rec, 2, table, 2))

                if any(th_cels_ids.count(element) > 1 for element in th_cels_ids):
                    ispassou = False
                    self.occurrences.add(OccurrenceInterface(self.rec, 3, table, 2))
            else:
                ispassou = False
                self.occurrences.add(OccurrenceInterface(self.rec, 1, table, 2))

            if th_cels_scope:
                if len(th_cels_scope) != len(th_cels):
                    ispassou = False
                    self.occurrences.add(OccurrenceInterface(self.rec, 5, table, 2))

                has_invalid_scope = False
                for scope in th_cels_scope:
                    if scope not in ['col', 'row', 'rowgroup', 'colgroup']:
                        has_invalid_scope = True
                        break

                if has_invalid_scope:
                    ispassou = False
                    self.occurrences.add(OccurrenceInterface(self.rec, 6, table, 2))
            else:
                ispassou = False
                self.occurrences.add(OccurrenceInterface(self.rec, 4, table, 2))

            if ispassou:
                self.occurrences.add(OccurrenceInterface(self.rec, 0, table, 2))

        return self.occurrences.list_of_occurrences
