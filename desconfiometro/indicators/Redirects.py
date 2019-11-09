import requests
from urllib.parse import urlparse, urlunparse
from desconfiometro.indicators.BaseIndicator import BaseIndicator
from desconfiometro.blueprints.models.Result import Result


class Redirects(BaseIndicator):
    def __init__(self):
        pass

    def get_name(self):
        return "Número de redirects"

    def get_description(self):
        return "Páginas com muitos redirects tendem a ser fraudulentas"

    def get_type(self):
        return "numeric"

    def evaluate(self, parsed_url):
        n = self.count_redirects(parsed_url)
        return None if (n == None) else Result(self.get_name(), self.get_description(), n, self.get_type())

    def count_redirects(self, parsed_url):
        try:
            response = requests.get(urlunparse(parsed_url))
            return len(response.history)
        except:
            return None

