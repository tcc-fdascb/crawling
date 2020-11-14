class Mining:
    """
    Análisa as ocorrências, extrai informações, calcula o índice de acessibilidade e guarda os resultados.
    """
    def __init__(self, occorrences, cities):
        self.occurrences = occorrences
        self.cities = cities

    def extractor(self):
        print('Iniciando cálculo com base nas ocorrências.')
        info = {}

        if not self.occurrences:
            print('<class Mining> Lista de ocorrências vazia.')

        for occurrence in self.occurrences:
            if occurrence['city_id'] in info.keys():
                info[occurrence['city_id']] = identify_info(occurrence, info[occurrence['city_id']])
            else:
                info[occurrence['city_id']] = identify_info(occurrence)

        for k in info.keys():
            for c in self.cities:
                city = self.cities[c]
                if k == city['_id']:
                    city['cms'] = info[k]['cms']
                    city['ia'] = calculate_ia(info[k]['errors'], info[k]['warnings'], info[k]['successes'])
                    city['errors'] = sum(info[k]['errors'])
                    city['warnings'] = sum(info[k]['warnings'])
                    city['successes'] = sum(info[k]['successes'])


def calculate_ia(errors, warnings, successes):
    """
    Cálcula o Índice de Acessibilidade

    fórmula: (p * ((ea / V) * (e / a * V) * w) / P
        p - Quantidade de páginas
        ea - Total de erros e alertas
        V - Total de verificações realizadas
        e - Total de erros
        a - Total de alertas
        w - Peso
        P - Somatória dos pesos

    :param errors: list<int>
    :param warnings: list<int>
    :param successes: list<int>
    :return: float
    """
    parcials = []
    for i in range(3):
        warnings_div = 1 if warnings[i] == 0 else warnings[i]
        total = 1 if errors[i] + warnings[i] + successes[i] == 0 else errors[i] + warnings[i] + successes[i]
        calculation = 1 * ((errors[i] + warnings[i]) / total) * ((errors[i] / warnings_div) / total) * (i + 1) / 6
        parcials.append(calculation)
    return round((1 - sum(parcials)) * 100, 1)


def identify_info(oc, dc=None):
    if dc is None:
        dc = {'cms': '', 'errors': [0, 0, 0], 'warnings': [0, 0, 0], 'successes': [0, 0, 0]}

    for i in range(3):
        if oc['peso'] == i + 1:
            if oc['type_code'] == 1:
                e = dc['errors'][i]
                dc['errors'][i] = e + 1
            elif oc['type_code'] == 2:
                w = dc['warnings'][i]
                dc['warnings'][i] = w + 1
            elif oc['type_code'] == 0:
                s = dc['successes'][i]
                dc['successes'][i] = s + 1

    if oc['tag'].startswith('CMS='):
        dc['cms'] = oc['tag'].replace('CMS=', '')

    return dc


if __name__ == '__main__':
    print(calculate_ia([0, 0, 0], [30, 98, 300], [30, 98, 300]))
    print(calculate_ia([27, 95, 388], [1, 2, 2], [2, 1, 10]))
