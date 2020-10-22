from bs4 import BeautifulSoup
import re

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface


class Recommendation03:
    """
        Recomendação 03: Utilizar corretamente os níveis de cabeçalho
    """

    def __init__(self, sourcecode):
        self.rec = 3
        self.sourcecode = sourcecode
        self.occurrences = Occurrences()

    def avaliacao(self):
        soup = BeautifulSoup(self.sourcecode, 'html.parser')
        is_pass = True

        tags_h1 = soup.find_all('h1')
        tags_h2 = soup.find_all('h2')
        tags_h3 = soup.find_all('h3')
        tags_headings = []
        tags_headings_name = []

        if not tags_h1:
            is_pass = False
            self.occurrences.add(OccurrenceInterface(self.rec, 1, '', 2))
        else:
            if not tags_h2 and not tags_h3:
                is_pass = False
                self.occurrences.add(OccurrenceInterface(self.rec, 2, '', 2))

        for tag in soup.find_all(re.compile("^h\d")):
            tags_headings.append(tag)
            tags_headings_name.append(int(tag.name.replace('h', '')))

        for i, t in enumerate(tags_headings_name):
            if i + 1 == len(tags_headings_name):
                break

            if tags_headings_name[i + 1] == t + 2 or \
                    tags_headings_name[i + 1] == t + 3 or \
                    tags_headings_name[i + 1] == t + 4 or \
                    tags_headings_name[i + 1] == t + 5:
                is_pass = False
                self.occurrences.add(OccurrenceInterface(self.rec, 3, f'{tags_headings[t]};{tags_headings[i + 1]}', 2))

        if is_pass:
            self.occurrences.add(OccurrenceInterface(self.rec, 0, '', 2))

        return self.occurrences.list_of_occurrences
