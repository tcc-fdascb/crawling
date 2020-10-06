import pandas as pd


def translate_message(messages, recommendation, code_message):
    code = ['OK', 'ERRO', 'ALERTA']
    for message in messages:
        if messages[message]['recommendation'] == recommendation and messages[message]['code_message'] == code_message:
            return code[messages[message]['type_feedback']] + ': ' + messages[message]['message']


class Occurrences:
    """
    Organiza as ocorrências em uma lista e trata sua exibição
    """
    def __init__(self):
        self.list_of_occurrences = []
        self.code_message = []
        self.list_code_recommendation = []
        self.list_peso = []
        self.list_type_feedback = []

    def add(self, occurrence):
        self.list_of_occurrences.append(occurrence)

    def show(self):
        messages = pd.read_csv('data/messages.csv').to_dict(orient='index')

        if len(self.list_of_occurrences) > 0 and self.list_of_occurrences[0][0] is not None:
            print("Lista de ocorrências:")
            for occurrence in self.list_of_occurrences:
                for key in occurrence.keys():
                    for value in occurrence.get(key):
                        self.code_message.append(value.code_message)
                        self.list_code_recommendation.append(value.recommendation)
                        print(value.recommendation,
                              value.code_message,
                              translate_message(messages, value.recommendation, value.code_message),
                              value.tag)
        qtd_rec = len(set(self.list_code_recommendation))
        cont0 = self.code_message.count(0)
        cont1 = self.code_message.count(1)
        cont2 = self.code_message.count(2)
        nota_site = int(((cont1 + cont2 + cont0) / qtd_rec) * 10)

        print('','Resultados:','A quantidade de  atributos validados = ' + str(cont0), 'A quantidade de avisos = ' + str(cont1),
                      'A quantidade de erros críticos= ' + str(cont2), 'Recomendações = ' + str(qtd_rec),
                      'Nota = ' + str(nota_site), sep='\n')

