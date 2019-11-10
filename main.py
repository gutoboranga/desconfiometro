from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

from desconfiometro.indicators.Redirects import Redirects
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

from desconfiometro.indicators.CNPJ import CNPJ

parsed = urlparse('htps://www.submarino.com.br')
print(parsed.netloc)

# sc = ReclameAqui()
# print(sc.get_name(), "Ok" if sc.evaluate(parsed) else "Not ok")

cnpj = CNPJ()
print(cnpj.evaluate(parsed, get_registro_br(parsed.netloc)).data)

# red = Redirects()
# print("redirects: ", red.evaluate(parsed).value)
