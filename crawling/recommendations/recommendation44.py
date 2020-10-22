from bs4 import BeautifulSoup

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface


class Recommendation44:
    """
        Recomendação 44: Agrupar campos de formulário
    """
    def __init__(self, sourcecode):
        self.rec = 44
        self.sourcecode = sourcecode
        self.occurrences = Occurrences()

    def avaliacao(self):
        soap = BeautifulSoup(self.sourcecode, 'html.parser')
        forms = soap.find_all('form')
        selects = soap.select('select')

        if forms:
            for form in forms:
                has_fieldset = True
                has_legend = True
                fieldsets = form.find_all('fieldset')

                if not fieldsets:
                    has_fieldset = False
                    self.occurrences.add(OccurrenceInterface(self.rec, 2, form, 2))
                else:
                    for fieldset in fieldsets:
                        if not fieldset.find('legend'):
                            has_legend = False
                            self.occurrences.add(OccurrenceInterface(self.rec, 3, form, 2))
                            break

                if has_fieldset and has_legend:
                    self.occurrences.add(OccurrenceInterface(self.rec, 0, form, 2))

        if selects:
            for select in selects:
                options = select.find_all('option')
                if len(options) > 5 and select.find('optgroup'):
                    self.occurrences.add(OccurrenceInterface(self.rec, 4, select, 2))
                else:
                    self.occurrences.add(OccurrenceInterface(self.rec, 1, select, 2))

        return self.occurrences.list_of_occurrences
