import requests


class Recommendation01:
    """
        Recomendação 01: Validar Html e CSS do Sitio Eletrônico


    """
    def __init__(self, content):
        self.content = content


    def validarcss(self):
        #htmlanalizer = requests.get('http://jigsaw.w3.org/css-validator/validator?uri='+str(self.content)+'&profile=css3svg&warning=0&output=soap12')
        cssanalizer = requests.get('http://jigsaw.w3.org/css-validator/validator?uri=www.google.com.br&profile=css3svg&warning=0&output=text')
        if cssanalizer.status_code == 200:
            print(cssanalizer.headers)
            print(cssanalizer.text)

    def validarhtml(self):
        htmlanalizer = requests.get('http://validator.w3.org/nu/?doc='+str(self.content)+'&out=text')
        if htmlanalizer.status_code == 200:
            print(htmlanalizer.text)

