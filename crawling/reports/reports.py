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
        df.to_csv(f'output/{dt.now().strftime(self.date_format)}_evaluation.csv', index=False)

    def detailed_occurrences(self):
        df = pd.DataFrame(self.occorrences)
        df.to_csv(f'output/{dt.now().strftime(self.date_format)}_occurrences.csv', index=False)
