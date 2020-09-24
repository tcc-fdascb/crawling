from bs4 import BeautifulSoup

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface


class Recommendation20:
    """
    Recomendação 20: Fornecer alternativa em texto para as imagens do sítio

    Verificações:
        - Imagens sem descrição (sem alt)
        - Imagens decorativas
        - Imagens com descrição longas
        - Imagem com dupla descrição, title e alt iguais
        - Imagens com descrição inadequada (nome do arquivo, “alt”, “descrição”, “imagem”, etc)
        - Imagens diferentes com a mesma descrição
    """

    def __init__(self, sourcecode):
        self.rec = 20
        self.occurrences = Occurrences()
        self.sourcecode = sourcecode

    def avaliacao(self):
        soap = BeautifulSoup(self.sourcecode, 'html.parser')
        imagens = soap.find_all('img')
        imagens_alt = []

        for imagem in imagens:
            has_error_or_warning = False

            # Imagens com conteúdo sem descrição (sem alt)
            if not imagem.has_attr('alt'):
                self.occurrences.add(OccurrenceInterface(self.rec, 1, imagem))
                has_error_or_warning = True
            else:
                # Imagens decorativas
                if imagem['alt'] == '':
                    self.occurrences.add(OccurrenceInterface(self.rec, 2, imagem))
                    has_error_or_warning = True

                # Imagens com descrição longas
                if len(imagem['alt']) > 140:
                    self.occurrences.add(OccurrenceInterface(self.rec, 3, imagem))
                    has_error_or_warning = True

                # Imagem com dupla descrição, title e alt iguais
                if 'title' in imagem.attrs:
                    if imagem['alt'] == imagem['title']:
                        self.occurrences.add(OccurrenceInterface(self.rec, 4, imagem))
                        has_error_or_warning = True

                # Imagens com descrição inadequada
                for desc in ['figura', 'imagem', 'image', 'img', 'alt', 'descrição', 'desc', 'foto', 'photo', 'picture', 'pic']:
                    if desc == imagem['alt']:
                        self.occurrences.add(OccurrenceInterface(self.rec, 5, imagem))
                        has_error_or_warning = True

                # Imagens diferentes com a mesma descrição
                imagens_alt.append(imagem['alt'])
                if imagem['alt'] != '' and imagem['alt'] in imagens_alt[:-1]:
                    self.occurrences.add(OccurrenceInterface(self.rec, 6, imagem))
                    has_error_or_warning = True

            # Não encontrou erros
            if not has_error_or_warning:
                self.occurrences.add(OccurrenceInterface(self.rec, 0, imagem))

        return self.occurrences.list_of_occurrences
