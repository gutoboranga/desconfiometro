from urllib.parse import urlparse

from desconfiometro.indicators.Certificate import Certificate
from desconfiometro.indicators.Greenlist import Greenlist
from desconfiometro.indicators.SpecialCharacters import SpecialCharacters

parsed = urlparse('http://localhost:5000/')

gl = Greenlist()
print(gl.evaluate(parsed))

crt = Certificate()
print(crt.evaluate(parsed))

sc = SpecialCharacters()
print(sc.evaluate(parsed))
