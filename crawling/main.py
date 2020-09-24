import requests
from threading import Thread
import pandas as pd
import urllib.robotparser
from datetime import datetime as dt

from crawling.recommendations import *
from crawling.occurrences import Occurrences

from crawling.recommendations.RecommendationEmag19 import  RecommendationEmag19
from crawling.recommendations.RecommendationEmag31 import RecommendationEmag31
from crawling.recommendations.RecommendationEmag39 import RecommendationEmag39
from crawling.recommendations.RecommendationEmag51 import RecommendationEmag51
from crawling.recommendations.RecommendationEmag61 import  RecommendationEmag61

# Define o arquivo de entrada
CSV_FILE = 'data/cities-abc.csv'

# Inicializa uma estância para lista de ocorrências
occurrences = Occurrences()


def csv_file_to_dict(file):
    try:
        data = pd.read_csv(file)
        data = data.to_dict(orient='index')
        return data
    except Exception:
        raise


class ValidateCity(Thread):
    """
    Conjunto de métodos para aplicação de Threads e avaliações para os sítios eletrônicos.
    """

    def __init__(self, city):
        Thread.__init__(self)
        self.city = city
        self.sourcecode = self.get_sourcecode()

    def run(self):
        self.validate_robots()

    def get_sourcecode(self):
        """
        Faz requisição do código fonte da página inicial do sítio eletrônico.
        Se bem sucedido, guarda duas novas keys no dict da cidade correspondente:
            - date_sourcecode: timestamp da requisição
            - sourcecode: conteúdo da resposta da requisição

        :return: <Response>.content OR None
        """
        try:
            self.sourcecode = requests.get(self.city['url'], timeout=30)

            if self.sourcecode.status_code == 200:
                self.city['date_sourcecode'] = dt.timestamp(dt.now())
                # self.city['sourcecode'] = self.sourcecode.content
                return self.sourcecode.content

            return None

        except requests.exceptions.RequestException as error:
            print(dt.timestamp(dt.now()), self.city['city_name'], error)

    def validate_robots(self):
        """
        Confere o arquivo robots.txt dos sites e verifica condições de Dissalow
        adicionando duas keys novas ao dict da cidade correspondente:
            - has_robotstxt (True/False): responde a pergunta se tem ou não o arquivo robots.txt
            - can_crawling (True/False): responde a pergunta se pode ou não fazer crawling
        """

        try:
            self.city['has_robotstxt'] = False
            self.city['can_crawling'] = True

            city_url = self.city['url']
            city_url_robots = city_url + 'robots.txt'

            robotstxt = requests.get(city_url_robots, timeout=30)

            if robotstxt.status_code == 200:
                self.city['has_robotstxt'] = True

                robotparser = urllib.robotparser.RobotFileParser()
                robotparser.set_url(city_url_robots)
                robotparser.read()

                if robotparser.can_fetch('*', city_url):
                    self.city['can_crawling'] = True

            if self.city['can_crawling']:
                self.validate_recommendations()

        except requests.exceptions.RequestException as error:
            print(dt.timestamp(dt.now()), self.city['city_name'], error)

    def validate_recommendations(self):
        """
        A partir do código fonte da página inicial do sítio eletrônico, valida as
        recomendações listadas e guarda suas ocorrências na lista de ocorrências.
        """

        if self.sourcecode:
            rec01_html = Recommendation01(self.sourcecode, url=self.city['url']).validar_css()
            occurrences.add({self.city['_id']: rec01_html})

            rec01_css = Recommendation01(self.sourcecode, url=self.city['url']).validar_html()
            occurrences.add({self.city['_id']: rec01_css})

            recemag19 = RecommendationEmag19(self.sourcecode).avaliacao()
            occurrences.add({self.city['_id']: recemag19})
            recemag61 = RecommendationEmag61(self.sourcecode).avaliacao()
            occurrences.add({self.city['_id']: recemag61})
            recemag31 = RecommendationEmag31(self.sourcecode).avaliacao()
            occurrences.add({self.city['_id']: recemag31})
            recemag39 = RecommendationEmag39(self.sourcecode).avaliacao()
            occurrences.add({self.city['_id']: recemag39})
            recemag51 = RecommendationEmag51(self.sourcecode).avaliacao()
            occurrences.add({self.city['_id']: recemag51})
            rec20 = Recommendation20(self.sourcecode).avaliacao()
            occurrences.add({self.city['_id']: rec20})


cities = csv_file_to_dict(CSV_FILE)
print(cities)

for c in cities:
    validate = ValidateCity(cities[c])
    validate.start()
    validate.join()

print(cities)

# Exibe ocorrências
occurrences.show()
