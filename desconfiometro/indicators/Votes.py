import requests
from urllib.parse import urlparse, urlunparse
from desconfiometro.indicators.BaseIndicator import BaseIndicator
from desconfiometro.blueprints.models.Result import Result
from desconfiometro.indicators.data.NegativeVotesRepository import NegativeVotesRepository
from desconfiometro.indicators.data.PositiveVotesRepository import PositiveVotesRepository


class Votes(BaseIndicator):
    def __init__(self):
        self.negative_votes_repository = NegativeVotesRepository()
        self.positive_votes_repository = PositiveVotesRepository()

    def get_name(self):
        return "Votos da Comunidade"

    def get_description(self):
        return "Desconfie de sites mal avaliados pela comunidade"

    def get_type(self):
        return "tuple"

    def evaluate(self, parsed_url):
        negative = self.negative_votes_repository.get_votes(parsed_url.netloc)
        positive = self.positive_votes_repository.get_votes(parsed_url.netloc)
        
        if negative == 0 and positive == 0:
            return None
        
        if positive > 0:
            score = (negative / positive) * 10
        else:
            score = 0
        
        r = Result(self.get_name(),
                      self.get_description(),
                      score,
                      self.get_type())
                      
        r.data = (negative, positive)
        
        return r
                     
