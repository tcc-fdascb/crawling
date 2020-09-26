from bs4 import BeautifulSoup

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface


class Recommendation06:
    """
    Recomendação 6: Fornecer âncoras para ir direto a um bloco de conteúdo
    """

    def __init__(self, sourcecode):
        self.rec = 6
        self.occurrences = Occurrences()
        self.sourcecode = sourcecode
