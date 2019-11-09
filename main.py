from urllib.parse import urlparse
import requests

from desconfiometro.indicators.Certificate import Certificate
from desconfiometro.indicators.Greenlist import Greenlist
from desconfiometro.indicators.DNS import DNS
from desconfiometro.indicators.SpecialCharacters import SpecialCharacters

parsed = urlparse('https://www.submaarino.com.br')
print(parsed.netloc)

gl = Greenlist()
print(gl.get_name(), "Ok" if gl.evaluate(parsed) else "Not ok")

crt = Certificate()
print(crt.get_name(), "Ok" if crt.evaluate(parsed) else "Not ok")

sc = SpecialCharacters()
print(sc.get_name(), "Ok" if sc.evaluate(parsed) else "Not ok")

ip = DNS()
print(ip.get_name(), "Ok" if ip.evaluate(parsed) else "Not ok")

