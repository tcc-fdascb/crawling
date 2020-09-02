import requests
import pandas as pd
import urllib.robotparser

from crawling.recommendations import *
from crawling.occurrences import Occurrences


# Inicializa uma estância para lista de ocorrências
occurrences = Occurrences()


# Faz leitura do arquivo CSV e converte para dict
cities = pd.read_csv('data/cities-sa.csv')
cities = cities.to_dict(orient='index')
print(cities)


# Confere o arquivo robots.txt dos sites e verifica condições de Dissalow adicionando duas keys novas ao dict cities:
#   - has_robotstxt (True/False) - responde a pergunta se tem ou não o arquivo robots.txt
#   - can_crawling (True/False) - responde a pergunta se pode ou não fazer crawling
for city in cities:
    cities[city]['has_robotstxt'] = False
    cities[city]['can_crawling'] = False

    city_url = cities[city]['url']
    city_url_robots = city_url + 'robots.txt'
    robotstxt = requests.get(city_url_robots)

    if robotstxt.status_code == 404:
        cities[city]['can_crawling'] = False

    if robotstxt.status_code == 200:
        cities[city]['has_robotstxt'] = True

        robotparser = urllib.robotparser.RobotFileParser()
        robotparser.set_url(city_url_robots)
        robotparser.read()

        if robotparser.can_fetch('*', city_url):
            cities[city]['can_crawling'] = True


# Se puder fazer o crawling, faz request do Código Fonte da home dos sites e guarda em nova key do dict cities
# A respeito do tipo de resposta da requisição:
# .text = identificação automatica da resposta
# .content = resposta em binário
# https://2.python-requests.org/en/master/user/quickstart/#response-content
for city in cities:
    cities[city]['sourcecode'] = None

    if cities[city]['can_crawling']:
        sourcecode = requests.get(cities[city]['url'])

        if sourcecode.status_code == 200:
            cities[city]['sourcecode'] = sourcecode.content

            # rec01 = Recommendation01(cities[city]['url']).validarhtml()
            # occurrences.add({'rec01': rec01})

            rec20 = Recommendation20(cities[city]['sourcecode']).avaliacao()
            occurrences.add({'rec20': rec20})


# Exibe ocorrências
occurrences.show()
