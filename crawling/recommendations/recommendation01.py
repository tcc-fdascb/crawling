from bs4 import BeautifulSoup
from string import Template
import re
import requests
from urllib.parse import quote, urlparse

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface

WEBSERVICE_CSS = 'http://jigsaw.w3.org/css-validator/validator?uri=$url&profile=css3&warning=0&output=json'
WEBSERVICE_HTML = 'http://validator.w3.org/nu/?doc=$url&out=json'


def encode_url(t):
    return quote(t, safe='')


class Recommendation01:
    """
        Recomendação 01: Validar HTML e CSS do sitio eletrônico
        - CSS: se o atributo "validity" for true, a folha de estilo é válida
        - HTML: se não houver em "messages" o tipo "error", o documento é válido
    """

    def __init__(self, content, url):
        self.rec = 1
        self.content = content
        self.url = url
        self.occurrences = Occurrences()

    def validar_css(self):
        soup = BeautifulSoup(self.content, 'html.parser')
        link_tags = soup.find_all('link')

        for link_tag in link_tags:
            href = link_tag.get('href')

            if self.url not in href:
                href = self.url + href

            if re.search('(app|main|styles?|global|estilos?|default).css', href) is not None \
               and re.search('plugins?|libs?|portlet|bootstrap|materialize', href) is None:
                url = Template(WEBSERVICE_CSS).substitute(url=encode_url(href))
                analizer = requests.get(url)

                if analizer.status_code == 200:
                    res = analizer.json()
                    if res['cssvalidation']['validity']:
                        self.occurrences.add(OccurrenceInterface(self.rec, 2, link_tag, 2))
                    else:
                        self.occurrences.add(OccurrenceInterface(self.rec, 3, link_tag, 2))

        return self.occurrences.list_of_occurrences

    def validar_html(self):
        is_valid = True
        url = Template(WEBSERVICE_HTML).substitute(url=encode_url(self.url))
        analizer = requests.get(url)

        if analizer.status_code == 200:
            res = analizer.json()

            for msg in res['messages']:
                if msg['type'] == 'error':
                    is_valid = False
                    break

        if is_valid:
            self.occurrences.add(OccurrenceInterface(self.rec, 0, '', 1))
        else:
            self.occurrences.add(OccurrenceInterface(self.rec, 1, '', 1))

        return self.occurrences.list_of_occurrences
