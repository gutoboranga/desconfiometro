import requests
from urllib.parse import urlparse, urlunparse
from desconfiometro.indicators.BaseIndicator import BaseIndicator
from desconfiometro.blueprints.models.Result import Result


class Redirects(BaseIndicator):
    def __init__(self):
        pass

    def get_name(self):
        return "Número de redirecionamentos"

    def get_description(self):
        return "Um alto número de redirecionamentos pode indicar que página é fraudulenta"

    def get_type(self):
        return "numeric"

    def make_score(self, count):
        if count == 0:
            return 10
        if count <= 3:
            return (1 / count) * 9
        if count > 3:
            return 0

    def evaluate(self, parsed_url, registro_br):
        n = self.count_redirects(parsed_url)
        return None if (n is None) else Result(self.get_name(), self.get_description(), self.make_score(n), self.get_type())

    def count_redirects(self, parsed_url):
        try:
            response = requests.get(urlunparse(parsed_url))
            return self.make_score(len(response.history))
        except Exception as e:
            print(e)
            return None
