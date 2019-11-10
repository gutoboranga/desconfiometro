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
               "boa reputação é fundamental"

    def get_type(self):
        return "ra"

    def make_score(self, rating):
        return rating

    def evaluate(self, parsed_url, registro_br):
        print("WILL GET RATING")
        x = self.scrap(parsed_url.netloc)

        if x == None:
            return None
        else:
            rating = x[0]
            name = x[1]
            r = Result(self.get_name(), self.get_description(), self.make_score(rating), self.get_type())
            r.data = name
            return r

    def scrap(self, netloc):
        try:
            chrome_options = Options()
            chrome_options.add_argument("--headless")

            driver = webdriver.Chrome(chrome_options=chrome_options)
            url = "https://www.reclameaqui.com.br/busca/?q=" + netloc
            driver.get(url)

            html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
            soup = BeautifulSoup(html, 'html.parser')

            # cards = soup.find_all(class_='card-list-search ng-scope slick-slide slick-current slick-active')
            # card_soup = BeautifulSoup(cards[0], 'html.parser')
            #
            cards = soup.find_all(class_='card-list-search ng-scope slick-slide slick-current slick-active')
            card = cards[0]
            items = card.text.strip().split('    ')

            name = items[1].strip()
            rating = float(items[8].strip())

            # name = card_soup.find_all(class_='hidden-xs')[0].text.strip()
            # rating = float(card_soup.find_all(class_='score-search col-md-3 ng-binding ng-scope')[0].text.strip())

            return rating, name
        except:
            return None
