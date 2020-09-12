from bs4 import BeautifulSoup
import itertools
from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface


class Recommendation20:
    """
    Recomendação 20: Fornecer alternativa em texto para as imagens do sítio

    Verificações:
        - Imagens com conteúdo sem descrição
        - Imagens com descrição inadequada
        - Imagens diferentes com a mesma descrição
        - Imagem com dupla descrição, title e alt iguais
        - Imagens com descrições longas no alt
    """

    def __init__(self, sourcecode):
        self.rec = 20
        self.occurrences = Occurrences()
        self.sourcecode = sourcecode

    def avaliacao(self):
        soap = BeautifulSoup(self.sourcecode, 'html.parser')
        imagens = soap.find_all('img')

        for imagem in imagens:
            if not imagem.has_attr('alt') or not imagem['alt']:
                self.occurrences.add(OccurrenceInterface(self.rec, 1, imagem))
            else:
                self.occurrences.add(OccurrenceInterface(self.rec, 0, imagem))

            if len(imagem['alt']) > 100:
                self.occurrences.add(OccurrenceInterface(self.rec, 2, imagem))

            for i in ["figura", "imagem", "alt", "descrição", "foto"]:
                if i == imagem['alt']:
                    self.occurrences.add(OccurrenceInterface(self.rec, 0, imagem))

            if imagem['alt'] == imagem['title']:
                self.occurrences.add(OccurrenceInterface(self.rec, 0, imagem))


        for compara1,compara2 in itertools.combinations(imagens,2):

            if compara1['alt'] == compara2['alt'] and compara1['src'] != compara2['src']:
                self.occurrences.add(OccurrenceInterface(self.rec, 2, imagem))


        return self.occurrences.list_of_occurrences
