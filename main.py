from urllib.parse import urlparse

from desconfiometro.indicators.Certificate import Certificate
from desconfiometro.indicators.Greenlist import Greenlist
from desconfiometro.indicators.IP import IP
from desconfiometro.indicators.SpecialCharacters import SpecialCharacters

parsed = urlparse('https://www.submarinoviagens.com.br')
print(parsed.netloc)

gl = Greenlist()
print(gl.get_name(), "Ok" if gl.evaluate(parsed) else "Not ok")

crt = Certificate()
print(crt.get_name(), "Ok" if crt.evaluate(parsed) else "Not ok")

sc = SpecialCharacters()
print(sc.get_name(), "Ok" if sc.evaluate(parsed) else "Not ok")

ip = IP()
print(ip.get_name(), "Ok" if ip.evaluate(parsed) else "Not ok")
