import pandas as pd


def translate_message(messages, recommendation, code_message):
    code = ['OK', 'ERRO', 'ALERTA']
    for message in messages:
        if messages[message]['recommendation'] == recommendation and messages[message]['code_message'] == code_message:
            return {
                'type_code': messages[message]['type_feedback'],
                'type': code[messages[message]['type_feedback']],
                'message': messages[message]['message']
            }


class Occurrences:
    """
    Organiza as ocorrências em uma lista e trata sua exibição
    """
    def __init__(self):
        self.list_of_occurrences = []

    def add(self, occurrence):
        self.list_of_occurrences.append(occurrence)

    def is_empty(self):
        if len(self.list_of_occurrences) > 0:
            return False
        return True

    def convert(self):
        messages = pd.read_csv('data/messages.csv').to_dict(orient='index')

        if self.is_empty():
            print('<class Occurrences> Converção impossível. Lista de ocorrências vazia.')
            return []

        list_of_dict = []
        for occurrence in self.list_of_occurrences:
            for key in occurrence.keys():
                for value in occurrence.get(key):
                    message = translate_message(messages, value.recommendation, value.code_message)
                    message = message if message else {'type_code': '', 'type': '', 'message': ''}
                    tag = str(value.tag).replace('\n', '')
                    list_of_dict.append({
                        'city_id': key,
                        'recommendation': value.recommendation,
                        'type_code': message['type_code'],
                        'type': message['type'],
                        'message': message['message'],
                        'message_code': value.code_message,
                        'tag': tag,
                        'peso': value.peso
                    })
        return list_of_dict

    def show_log(self):
        if self.is_empty():
            print('<class Occurrences> Não há o que ser mostrado. Lista de ocorrências vazia.')
            return False

        dicts = self.convert()
        print('\n----------------- LOG START -----------------')
        for i, d in enumerate(dicts):
            print(f'#{i} | '
                  f'City ID {d["city_id"]} | '
                  f'REC {d["recommendation"]} | '
                  f'Type({d["type_code"]}): {d["type"]} | '
                  f'Message({d["message_code"]}): {d["message"]} | '
                  f'Tag: {d["tag"]} | '
                  f'Peso: {d["peso"]}'
                  )
        print('----------------- LOG END -----------------\n')
        return True
