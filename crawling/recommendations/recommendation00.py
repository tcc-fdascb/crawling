import wad

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface


class Recommendation00:
    """
    Recomendação 0: Identifica o CMS utilizado na construção do sítio eletrônico
    """

    def __init__(self, url):
        self.rec = 0
        self.url = url
        self.occurrences = Occurrences()

    def identify(self):
        try:
            if self.url:
                techs = wad.Detector().detect(self.url)
                for tech in techs[self.url]:
                    if tech['type'] and 'cms' in tech['type'].lower():
                        self.occurrences.add(OccurrenceInterface(self.rec, 1, f'CMS={tech["app"]}', 0))

                if len(self.occurrences.list_of_occurrences) == 0:
                    self.occurrences.add(OccurrenceInterface(self.rec, 0, '', 0))

                return self.occurrences.list_of_occurrences
        except Exception as e:
            print('REC00 - CMS: ERROR', e)


if __name__ == '__main__':
    Recommendation00('https://www2.santoandre.sp.gov.br/').identify()
