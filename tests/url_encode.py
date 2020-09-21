import urllib.parse
from string import Template

o = urllib.parse.quote('http://flaviodutra.com.br/?q=o loko meu', safe='')
print(o)

t = Template('http://flaviodutra.com.br/?url=$url&out=$format').substitute(url='google.com', format='json')
print(urllib.parse.quote(t, safe=''))
