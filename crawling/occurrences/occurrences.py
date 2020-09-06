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

    def add(self, occurrence):
        self.list_of_occurrences.append(occurrence)

    def show(self):
        messages = pd.read_csv('data/messages.csv').to_dict(orient='index')

        print("Lista de ocorrências:")
        for occurrence in self.list_of_occurrences:
            for key in occurrence.keys():
                print(key)
                for value in occurrence.get(key):
                    print(value.recommendation,
                          value.code_message,
                          translate_message(messages, value.recommendation, value.code_message),
                          value.tag)
