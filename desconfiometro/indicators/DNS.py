from desconfiometro.indicators.BaseIndicator import BaseIndicator
from desconfiometro.blueprints.models.Result import Result
from desconfiometro.indicators.utils import get_registro_br

import re


class DNS(BaseIndicator):

    def __init__(self):
        self.ip_regex = "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}"

    def get_name(self):
        return "DNS"
        
    def get_description(self):
        return "Confere se o endereço que aparece no \"link\" é registrado."

    def get_type(self):
        return "boolean"
        
    def make_score(self, ok):
        return 10 if ok else 0

    def evaluate(self, parsed_url):
        ok = None
        if not self.isIP(parsed_url.netloc):
            reg = get_registro_br(parsed_url.netloc)
            if reg != "":
                ok = True
            elif reg == "":
                ok = False
        return Result(self.get_name(), self.get_description(), self.make_score(ok), self.get_type())

    def isIP(self, netloc):
        return True if re.match(self.ip_regex, netloc) else False
