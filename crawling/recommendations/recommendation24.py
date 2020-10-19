from bs4 import BeautifulSoup
from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface

class Recommendation24:
    """
    Recomendação 24: Associar células de dados às células de cabeçalho


    Peso: 2
    """

    def __init__(self, sourcecode):
        self.rec = 24
        self.occurrences = Occurrences()
        self.sourcecode = sourcecode


    def avaliacao(self):
        ispassou = True
        soap = BeautifulSoup(self.sourcecode,'html.parser')
        table = soap.findAll('table')
        for tableitem in table:
            if tableitem.find_all('thead') and tableitem.find_all('tbody'):
                if not tableitem.find('tbody').find_previous_sibling('tfoot'):
                    err = tableitem.find('tbody')
                    self.occurrences.add(OccurrenceInterface(self.rec, 1, err, 2))
                    ispassou = False
            else:
                for item in tableitem.find_all('td'):
                    # if item['id'] or item['headers'] or item['scope'] or item['axis']:
                    attr = item.attrs
                    if 'id' in attr or 'headers' in attr or 'scope' in attr or 'axis' in attr:
                        pass
                    else:
                        ispassou = False
                        self.occurrences.add(OccurrenceInterface(self.rec, 2, item, 2))

                for item in tableitem.findAll('th'):
                    # if item['id'] or item['headers'] or item['scope'] or item['axis']:
                    attr = item.attrs
                    if 'id' in attr or 'headers' in attr or 'scope' in attr or 'axis' in attr:
                        pass
                    else:
                        self.occurrences.add(OccurrenceInterface(self.rec, 2, item, 2))
                        ispassou = False


        if ispassou:
            self.occurrences.add(OccurrenceInterface(self.rec, 0, "", 2))

        return self.occurrences.list_of_occurrences
