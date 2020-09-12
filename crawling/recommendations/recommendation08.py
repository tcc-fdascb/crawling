from bs4 import BeautifulSoup , Comment
import re
from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface


class Recommendation08:
    """
    Recomendação 08: Separar links adjacentes
    """

    def __init__(self, sourcecode):
        self.rec = 8
        self.sourcecode = sourcecode
        self.occurrences = Occurrences()

    def avaliacao(self):


        soap = BeautifulSoup(self.sourcecode, 'html.parser')
        remove = soap.find_all(text=lambda text:isinstance(text, Comment))
        for removeitem in remove: #remove o código html comentado
            removeitem.extract()
        soapfiltro = BeautifulSoup(soap.prettify(), 'html.parser')

        for paragraph in soap.find_all('p'):
            tags_a = paragraph.find_all('a')
            if len(tags_a) > 1:
                par = str(paragrah).toLowerCase()
                paragrafosemespaco = re.sub('\s',"",par) #tira os espacos para verificar o "\n"

            if (par.find_in_text('</a><a')):  # verifica se tem um fechamento ligado na abertura de outra tag a
                # dispara erro

            if (par.find_in_text('</a> <a')):  # verifica se tem espaço entre fechamento e abertura de outra tag a
            # dispara erro

            if (par.find_in_text('</a><br><a') or par.find_in_text('</a><br /><a') or par.find_in_text('</a><br/><a')):
                # verifica se tem a tag de quebra de linha entre fechamento e abertura de outra tag a
            # dispara erro
            if paragrafosemespaco.find_in_text("</a>\n<a"):  # verifica se tem quebra de linha entra o fechamento e abertura de outra tag a
