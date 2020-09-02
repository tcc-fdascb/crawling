import pandas as pd
import requests

cities = pd.read_csv('../crawling/data/cities-abc.csv')
cities = cities.to_dict(orient='index')
# print(cities)

counter = 0

while True:
    for city in cities:
        try:
            # raise requests.exceptions.HTTPError('Throwing an exception here!')
            conex = requests.get(cities[city]['url'], timeout=5)
            # conex.raise_for_status()

            counter += 1
            print(counter, cities[city]['city_name'], conex.status_code)
            print('-----------')
        except requests.exceptions.RequestException as e:
            print('RequestException >>> ', e)
            print('xxxxxxxxxxx')
