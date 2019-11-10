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
        return self.get_rating(parsed_url.netloc)

    def get_rating(self, netloc):
        r = requests.get(url=netloc)
        data = r.content

        return Result(self.get_name(), self.get_description(), (1 if ok else 0), self.get_type())
