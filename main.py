from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


from desconfiometro.indicators.Certificate import Certificate
from desconfiometro.indicators.ReclameAqui import ReclameAqui
from desconfiometro.indicators.Greenlist import Greenlist
from desconfiometro.indicators.DNS import DNS
from desconfiometro.indicators.SpecialCharacters import SpecialCharacters
from desconfiometro.indicators.data.VotesRepository import VotesRepository

parsed = urlparse('https://www.submarinoviagens.com.br')
print(parsed.netloc)

gl = Greenlist()
print(gl.get_name(), "Ok" if gl.evaluate(parsed) else "Not ok")

crt = Certificate()
print(crt.get_name(), "Ok" if crt.evaluate(parsed) else "Not ok")

sc = ReclameAqui()
print(sc.get_name(), "Ok" if sc.evaluate(parsed) else "Not ok")

vr = VotesRepository("negative_votes.txt")
print("votes: ", vr.get_votes(parsed.netloc))

ip = DNS()
print(ip.get_name(), "Ok" if ip.evaluate(parsed) else "Not ok")

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)

try:
    driver.get("https://www.reclameaqui.com.br/busca/?q=" + parsed.netloc)
    html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find_all(class_='score-search col-md-3 ng-binding ng-scope')
    
    first = divs[0]
    
    float(first.text.strip())
except:
    print("")
