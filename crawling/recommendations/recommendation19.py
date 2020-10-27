from bs4 import BeautifulSoup

from ..occurrences.occurrences import Occurrences
from ..occurrences.occurrence_interface import OccurrenceInterface


class Recommendation19:
    """
    Recomendação 19: Descrever links clara e sucintamente
    """

    def __init__(self, sourcecode):
        self.rec = 19
        self.sourcecode = sourcecode
        self.occurrences = Occurrences()

    def avaliacao(self):
        soup = BeautifulSoup(self.sourcecode, 'html.parser')
        links = soup.find_all('a')

        if links:
            all_contents = []
            all_hrefs = []

            for link in links:
                is_pass = True
                imgs = link.find_all('img')
                contents = link.contents
                href = link.get('href')
                words = ['clique aqui', 'leia mais', 'veja aqui', 'veja mais', 'mais', 'saiba mais', 'acesse a lista']
                file_extensions = ['mp3', 'ogg', '7z', 'rar', 'zip', 'csv', 'xml', 'exe', 'msi', 'apk',
                                   'odp', 'pps', 'ppt', 'ods', 'xls', 'avi', 'mp4', 'mpg', 'mpeg', 'doc',
                                   'odt', 'pdf']

                if not contents and (not link.has_attr('title') or link.get('title') == ''):
                    is_pass = False
                    self.occurrences.add(OccurrenceInterface(self.rec, 1, link, 2))

                if not contents and link.has_attr('title') and link.get('title') != '':
                    is_pass = False
                    self.occurrences.add(OccurrenceInterface(self.rec, 2, link, 2))

                if contents and link.has_attr('title') and link.get('title') != '':
                    is_pass = False
                    self.occurrences.add(OccurrenceInterface(self.rec, 3, link, 2))

                if link.has_attr('title') and link.get('title') != '':
                    if link.get('title').lower() in words:
                        is_pass = False
                        self.occurrences.add(OccurrenceInterface(self.rec, 4, link, 2))

                if contents:
                    for content in contents:
                        if str(content).lower() in words:
                            is_pass = False
                            self.occurrences.add(OccurrenceInterface(self.rec, 5, link, 2))
                            break

                if imgs:
                    for img in imgs:
                        if not img.has_attr('alt') or img.get('alt') == '':
                            is_pass = False
                            self.occurrences.add(OccurrenceInterface(self.rec, 6, link, 2))

                if contents in all_contents:
                    is_pass = False
                    self.occurrences.add(OccurrenceInterface(self.rec, 7, link, 2))
                else:
                    all_contents.append(contents)

                if href in all_hrefs:
                    is_pass = False
                    self.occurrences.add(OccurrenceInterface(self.rec, 8, link, 2))
                else:
                    all_hrefs.append(href)

                if href and '.' in href:
                    ext = href.split('.')
                    if ext[1] in file_extensions and not ext[1] in str(contents):
                        is_pass = False
                        self.occurrences.add(OccurrenceInterface(self.rec, 9, link, 2))

                if is_pass:
                    self.occurrences.add(OccurrenceInterface(self.rec, 0, link, 2))

        return self.occurrences.list_of_occurrences
