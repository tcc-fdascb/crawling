from bs4 import BeautifulSoup
class Recommendation01:
    """
    Recomendação 1:Fornecer alternativa em texto para as imagens do sítio 
    Descrição da recomendação se houver

    :param name - Recebe o nome da Recomendação
    """

    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

    def Avaliacao(self, contents):
        #self.contents = contents
        soap = BeautifulSoup(contents,'html.parser')
        imagens = soap.find_all('img')
        
        for imagem in imagens:
            
            if imagem.has_attr('alt') == False :
                 print('Erro 2 :'+str(imagem)+'| Não possui o atributo "Alt"' )
            elif not imagem['alt'] :
                print('Erro 1 :'+str(imagem)+'| Não possui valor no atributo "Alt"' )     
        #print(imagens)           