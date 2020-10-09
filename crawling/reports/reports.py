import pandas as pd
from datetime import datetime as dt


class Reports:
    """
    Gera relatório com o resultado da avaliação de cada cidade e informações detalhadas das ocorrências.
    """

    def __init__(self, occorrences=None, cities=None):
        self.occorrences = occorrences
        self.cities = cities
        self.date_format = '%Y%m%d_%Hh%M'

    def cities_evaluation(self):
        cities = []
        for c in self.cities:
            cities.append(self.cities[c])
        df = pd.DataFrame(cities)
        df.to_csv(f'output/evaluation_{dt.now().strftime(self.date_format)}.csv', index=False)

    def detailed_occurrences(self):
        df = pd.DataFrame(self.occorrences)
        df.to_csv(f'output/occurrences_{dt.now().strftime(self.date_format)}.csv', index=False)


if __name__ == '__main__':
    mock_cities = {0: {'_id': 0, 'city_name': 'Santo André', 'url': 'https://www2.santoandre.sp.gov.br/', 'has_robotstxt': True, 'can_crawling': True, 'date_sourcecode': 1602200450.067669, 'wab': 1.53, 'errors': 2, 'warnings': 5, 'successes': 48}, 1: {'_id': 1, 'city_name': 'São Bernardo do Campo', 'url': 'https://www.saobernardo.sp.gov.br/', 'has_robotstxt': True, 'can_crawling': True, 'date_sourcecode': 1602200450.584301, 'wab': 5.33, 'errors': 4, 'warnings': 12, 'successes': 2}, 2: {'_id': 2, 'city_name': 'São Caetano do Sul', 'url': 'http://www.saocaetanodosul.sp.gov.br/', 'has_robotstxt': True, 'can_crawling': True, 'date_sourcecode': 1602200453.418873, 'wab': 0.33, 'errors': 1, 'warnings': 40, 'successes': 2}, 3: {'_id': 3, 'city_name': 'Diadema', 'url': 'http://www.diadema.sp.gov.br/', 'has_robotstxt': True, 'can_crawling': False}, 4: {'_id': 4, 'city_name': 'Mauá', 'url': 'http://www.maua.sp.gov.br/', 'has_robotstxt': False, 'can_crawling': True, 'date_sourcecode': 1602200453.81358, 'wab': 2.51, 'errors': 3, 'warnings': 23, 'successes': 30}, 5: {'_id': 5, 'city_name': 'Ribeirão Pires', 'url': 'http://www.ribeiraopires.sp.gov.br/', 'has_robotstxt': False, 'can_crawling': True, 'date_sourcecode': 1602200455.358584, 'wab': 1.33, 'errors': 2, 'warnings': 0, 'successes': 1}, 6: {'_id': 6, 'city_name': 'Rio Grande da Serra', 'url': 'http://www.riograndedaserra.sp.gov.br/', 'has_robotstxt': True, 'can_crawling': True, 'date_sourcecode': 1602200458.101188, 'wab': 0.33, 'errors': 1, 'warnings': 0, 'successes': 1}}
    reports = Reports(cities=mock_cities)
    reports.cities_evaluation()
