from desconfiometro.indicators.BaseIndicator import BaseIndicator
from desconfiometro.blueprints.models.Result import Result

import re


class IP(BaseIndicator):

    def __init__(self):
        self.ip_regex = "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}"

    def get_name(self):
        return "IP"
        
    def get_description(self):
        return "Confere se o IP bla bla bla"

    def get_type(self):
        return "boolean"

    def evaluate(self, parsed_url):
        return Result(self.get_name(), self.get_description(), not self.isIP(parsed_url.netloc), self.get_type())

    def isIP(self, netloc):
        return True if re.match(self.ip_regex, netloc) else False
