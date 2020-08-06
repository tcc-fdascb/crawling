from bs4 import BeautifulSoup


class Recommendation20:
    """
    Recomendação 20: Fornecer alternativa em texto para as imagens do sítio
    Descrição da recomendação se houver
    """

    def __init__(self, sourcecode):
        self.sourcecode = sourcecode

    def avaliacao(self):
        soap = BeautifulSoup(self.sourcecode, 'html.parser')
        imagens = soap.find_all('img')
        
        for imagem in imagens:
            if not imagem.has_attr('alt'):
                print(f'Erro 2: {str(imagem)} | Não possui o atributo "alt"')
            elif not imagem['alt']:
                print(f'Erro 1: {str(imagem)} | Não possui valor no atributo "alt"')
            # else:
            #     print(f'Ok: {str(imagem)}')

