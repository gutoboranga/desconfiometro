from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import requests
from desconfiometro.indicators.BaseIndicator import BaseIndicator
from desconfiometro.blueprints.models.Result import Result


class ReclameAqui(BaseIndicator):
    def __init__(self):
        pass

    def get_name(self):
        return "Nota no ReclameAqui"

    def get_description(self):
        return "O ReclameAqui reúne denúncias e resoluções de casos relatados por usuários, possuir um usuário e uma " \
               "boa reputação é fundamental."

    def get_type(self):
        return "numeric"

    def evaluate(self, parsed_url):
        print("WILL GET RATING")
        rating = self.get_rating(parsed_url.netloc)
        return None if (rating == None) else Result(self.get_name(), self.get_description(), rating, self.get_type())

    def get_rating(self, netloc):
        try:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            
            driver = webdriver.Chrome(chrome_options=chrome_options)
            url = "https://www.reclameaqui.com.br/busca/?q=" + netloc
            driver.get(url)
            
            html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
            soup = BeautifulSoup(html, 'html.parser')
            divs = soup.find_all(class_='score-search col-md-3 ng-binding ng-scope')
            
            first = divs[0]
            
            return float(first.text.strip())
        except:
            return None
