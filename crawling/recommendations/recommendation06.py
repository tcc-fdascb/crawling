from bs4 import BeautifulSoup

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface


class Recommendation06:
    """
    Recomendação 6: Fornecer âncoras para ir direto a um bloco de conteúdo

    Verificações:
        - O primeiro link deve conter # no href e não pode conter:
            - os termos “topo, voltar” no title ou href
            - href não pode ter valor igual à #
        - Verificar se há atributo style definido no link, no parent li ou ul; se houver, não pode conter as regras:
            - visibility: hidden;
            - display: none;
            - overflow: hidden;
    """

    def __init__(self, sourcecode):
        self.rec = 6
        self.occurrences = Occurrences()
        self.sourcecode = sourcecode

    def avaliacao(self):
        soap = BeautifulSoup(self.sourcecode, 'html.parser')
        links = soap.find_all('a')

        if links:
            first_link = links[0]
            has_error_or_warning = False

            if first_link.has_attr('href') and first_link['href'][0] == '#'\
                    and first_link['href'] != '#' and not is_back_to_top(first_link):
                link_has_bad_style = False
                parent_has_bad_style = False

                if first_link.has_attr('style') and has_bad_style(first_link['style']):
                    link_has_bad_style = True

                for parent in first_link.parents:
                    if parent.name != 'body':
                        if parent.has_attr('style') and has_bad_style(parent['style']):
                            parent_has_bad_style = True
                            break
                    else:
                        break

                if link_has_bad_style or parent_has_bad_style:
                    self.occurrences.add(OccurrenceInterface(self.rec, 2, first_link, 1))
                    has_error_or_warning = True
            else:
                self.occurrences.add(OccurrenceInterface(self.rec, 1, first_link, 1))
                has_error_or_warning = True

            if not has_error_or_warning:
                self.occurrences.add(OccurrenceInterface(self.rec, 0, first_link, 1))
                pass

        return self.occurrences.list_of_occurrences


def has_bad_style(s):
    rules = ['display:none', 'overflow:hidden', 'visibility:hidden']
    s = s.replace(' ', '').lower()
    for rule in rules:
        if rule in s:
            return True
    return False


def is_back_to_top(el):
    words = ['topo', 'voltar']
    s = str(el).replace(' ', '').lower()
    for word in words:
        if word in s:
            return True
    return False
