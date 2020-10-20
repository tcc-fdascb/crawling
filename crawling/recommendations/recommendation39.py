from bs4 import BeautifulSoup , Comment

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface


class Recommendation39:
    """
    Recomendação 39: Associar etiquetas aos seus campos
    """

    def __init__(self, sourcecode):
        self.rec = 39
        self.sourcecode = sourcecode
        self.occurrences = Occurrences()

    def avaliacao(self):
        soap = BeautifulSoup(self.sourcecode, 'html.parser')
        fields = []

        for field in soap.find_all('input'):
            field_type = field.get('type')
            if field_type == 'text' or \
                    field_type == 'file' or \
                    field_type == 'password' or \
                    field_type == 'radio' or \
                    field_type == 'checkbox':
                fields.append(field)

        for field in soap.find_all('textarea') + soap.find_all('select'):
            fields.append(field)

        for field in fields:
            if field.get('id'):
                if soap.select(f'label[for="{field.get("id")}"]'):
                    self.occurrences.add(OccurrenceInterface(self.rec, 0, field, 3))
                else:
                    self.occurrences.add(OccurrenceInterface(self.rec, 1, field, 3))
            else:
                self.occurrences.add(OccurrenceInterface(self.rec, 2, field, 3))

        return self.occurrences.list_of_occurrences
