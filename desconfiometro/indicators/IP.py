from desconfiometro.indicators.BaseIndicator import BaseIndicator
import re


class IP(BaseIndicator):

    def __init__(self):
        self.ip_regex = "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}"


    def get_name(self):
        return "IP"

    def get_type(self):
        return "boolean"

    def evaluate(self, parsed_url):
        return not self.isIP(parsed_url.netloc)

    def isIP(self, netloc):
        return True if re.match(self.ip_regex, netloc) else False
