from urllib.parse import urlparse

from desconfiometro.indicators.Greenlist import Greenlist

parsed = urlparse('https://www.submarinoviagens.com.br/index')

gl = Greenlist()
print(gl.evaluate(parsed))
