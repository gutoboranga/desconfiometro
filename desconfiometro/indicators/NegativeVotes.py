import requests
from urllib.parse import urlparse, urlunparse
from desconfiometro.indicators.BaseIndicator import BaseIndicator
from desconfiometro.blueprints.models.Result import Result


class NegativeVotes(BaseIndicator):
    def __init__(self):
        pass

    def get_name(self):
        return "Votos Negativos da Comunidade"

    def get_description(self):
        return "Desconfie de sites mal avaliados pela comunidade"

    def get_type(self):
        return "numeric"

    def evaluate(self, parsed_url):
        return Result(self.get_name(), self.get_description(), self.get_negative_votes(parsed_url), self.get_type())

    def count_redirects(self, parsed_url):
        response = requests.get(urlunparse(parsed_url))
        return len(response.history)

