import pandas as pd

from crawling.evaluation import Evaluation
from crawling.mining import Mining
from crawling.reports import Reports


# Define o arquivo de entrada
CSV_FILE = 'data/cities-abc.csv'
cities = pd.read_csv(CSV_FILE)
cities = cities.to_dict(orient='index')

threads = []
occurrences_by_cities = []
occurrences = []

for i, c in enumerate(cities):
    threads.insert(i, Evaluation(cities[c]))
    threads[i].start()

for i, thread in enumerate(threads):
    threads[i].join()
    occurrences_by_cities.append(threads[i].get_occurrences())

for occ in occurrences_by_cities:
    occurrences += occ

# Cálcula os score com base nas ocorrências
mining = Mining(occurrences, cities)
mining.extractor()

# Gera relatórios
reports = Reports(occurrences, cities)
reports.detailed_occurrences()
reports.cities_evaluation()
