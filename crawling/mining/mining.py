class Mining:
    """
    Análisa as ocorrências, extrai informações, calcula o índice de acessibilidade e guarda os resultados.
    """
    def __init__(self, occorrences, cities):
        self.occurrences = occorrences
        self.cities = cities

    def extractor(self):
        print('Iniciando cálculo com base nas ocorrências.')
        information = {}

        if not self.occurrences:
            print('<class Mining> Lista de ocorrências vazia.')

        for occurrence in self.occurrences:
            if occurrence['city_id'] in information.keys():
                information[occurrence['city_id']] = identify_info(occurrence, information[occurrence['city_id']])
            else:
                information[occurrence['city_id']] = identify_info(occurrence)

        for k in information.keys():
            for c in self.cities:
                city = self.cities[c]
                if k == city['_id']:
                    city['cms'] = information[k]['cms']
                    city['wab'] = round(calculate_wab(information[k]['errors'], information[k]['warnings']), 2)
                    city['errors'] = sum(information[k]['errors'])
                    city['warnings'] = sum(information[k]['warnings'])
                    city['successes'] = information[k]['successes']


def calculate_wab(es, ws):
    """
    Índice de Acessibilidade
    Fórmula WAB (Web Accessibility Barrier)

    fórmula: p * ea * (e / a) * w
        p - quantidade de páginas
        ea - total de erros e alertas
        e - total de erros
        a - total de alertas
        w - peso

    :param es: list<int>
    :param ws: list<int>
    :return: float
    """

    parcials = []
    for i in range(3):
        d = 1 if ws[i] == 0 else ws[i]
        c = 1 * ((es[i] + ws[i]) * (es[i] / d)) * (i + 1)
        parcials.append(c)
    return sum(parcials) / len(parcials)


def identify_info(oc, dc=None):
    if dc is None:
        dc = {'cms': '', 'errors': [0, 0, 0], 'warnings': [0, 0, 0], 'successes': 0}

    if oc['peso'] == 1:
        if oc['type_code'] == 1:
            e = dc['errors'][0]
            dc['errors'][0] = e + 1
        elif oc['type_code'] == 2:
            w = dc['warnings'][0]
            dc['warnings'][0] = w + 1
        elif oc['type_code'] == 0:
            dc['successes'] = dc['successes'] + 1
    elif oc['peso'] == 2:
        if oc['type_code'] == 1:
            e = dc['errors'][1]
            dc['errors'][1] = e + 1
        elif oc['type_code'] == 2:
            w = dc['warnings'][1]
            dc['warnings'][1] = w + 1
        elif oc['type_code'] == 0:
            dc['successes'] = dc['successes'] + 1
    elif oc['peso'] == 3:
        if oc['type_code'] == 1:
            e = dc['errors'][2]
            dc['errors'][2] = e + 1
        elif oc['type_code'] == 2:
            w = dc['warnings'][2]
            dc['warnings'][2] = w + 1
        elif oc['type_code'] == 0:
            dc['successes'] = dc['successes'] + 1

    if oc['tag'].startswith('CMS='):
        dc['cms'] = oc['tag'].replace('CMS=', '')

    return dc
