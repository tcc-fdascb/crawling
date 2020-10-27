from bs4 import BeautifulSoup
import validators

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface


class Recommendation11:
    """
    Recomendação 11: Não criar páginas com atualização automática periódica
    """

    def __init__(self, sourcecode):
        self.rec = 11
        self.sourcecode = sourcecode
        self.occurrences = Occurrences()

    def avaliacao(self):
        soap = BeautifulSoup(self.sourcecode, 'html.parser')

        metas = soap.select('meta[http-equiv]')

        for meta in metas:
            is_pass = True
            value = meta.get('http-equiv')
            content = meta.get('content')

            if value and value.lower() == 'refresh':
                print('META SENDO ANALISADA >>>', meta)
                if content and ';' in content:
                    content = str(content).lower().split(';')
                    if content[0] and content[0].isdigit() and int(content[0]) >= 0:
                        if content[1] and '=' in content[1]:
                            content_url = content[1].split('=')
                            url = content_url[1].replace('\'', '').replace('"', '')
                            if content_url[0] and url and (content_url[0] != 'url' or not validators.url(url)):
                                is_pass = False
                                self.occurrences.add(OccurrenceInterface(self.rec, 3, meta, 3))
                    else:
                        is_pass = False
                        self.occurrences.add(OccurrenceInterface(self.rec, 2, meta, 3))
                else:
                    is_pass = False
                    self.occurrences.add(OccurrenceInterface(self.rec, 1, meta, 3))

                if is_pass:
                    self.occurrences.add(OccurrenceInterface(self.rec, 0, meta, 3))

        return self.occurrences.list_of_occurrences
