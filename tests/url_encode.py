import urllib.parse
from urllib.parse import urlparse
from string import Template
import re

o = urllib.parse.quote('http://flaviodutra.com.br/?q=o loko meu', safe='')
print(o)

t = Template('http://flaviodutra.com.br/?url=$url&out=$format').substitute(url='google.com', format='json')
print(urllib.parse.quote(t, safe=''))


parse = urlparse('http://flaviodutra.com.br/../path/omg/tgif//meteoloko?url=$url&out=$format')
ls = [parse.scheme, '://', parse.netloc, re.sub('/\.*/', '/', parse.path), parse.params, parse.query, parse.fragment]
print(parse)
print(''.join(ls))
