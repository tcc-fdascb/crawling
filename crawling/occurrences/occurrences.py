class Occurrences:
    """
    Organiza as ocorrências em uma lista e trata sua exibição
    """

    def __init__(self):
        self.list_of_occurrences = []

    def add(self, occurrence):
        self.list_of_occurrences.append(occurrence)

    def show(self):
        print("Lista de ocorrências:")
        for occurrence in self.list_of_occurrences:
            for key in occurrence.keys():
                print(key)
                for value in occurrence.get(key):
                    print(value.code, value.message, value.tag)
