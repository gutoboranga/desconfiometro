from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
from desconfiometro.indicators.utils import get_registro_br

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


from desconfiometro.indicators.Certificate import Certificate
from desconfiometro.indicators.ReclameAqui import ReclameAqui
from desconfiometro.indicators.Greenlist import Greenlist
from desconfiometro.indicators.DNS import DNS
from desconfiometro.indicators.SpecialCharacters import SpecialCharacters
from desconfiometro.indicators.Votes import Votes
from desconfiometro.indicators.data.NegativeVotesRepository import NegativeVotesRepository
from desconfiometro.indicators.data.VotesRepository import VotesRepository

parsed = urlparse('https://www.submarinoviagens.com.br/index')
print(parsed.netloc)

gl = Greenlist()
print(gl.get_name(), "Ok" if gl.evaluate(parsed) else "Not ok")

# sc = ReclameAqui()
# print(sc.get_name(), "Ok" if sc.evaluate(parsed) else "Not ok")

ip = DNS()
print(ip.get_name(), ip.evaluate(parsed).value)

v = Votes()
print("votes: ", v.evaluate(parsed).value)
