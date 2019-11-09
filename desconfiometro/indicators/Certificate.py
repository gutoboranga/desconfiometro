import requests
from requests.exceptions import SSLError
from desconfiometro.indicators.BaseIndicator import BaseIndicator

class Certificate(BaseIndicator):

    def __init__(self):
        pass

    def get_name(self):
        return "Certificate"

    def get_type(self):
        return "boolean"

    def evaluate(self, parsed_url):
        return self.has_valid_certificate(parsed_url.netloc)

    def has_valid_certificate(self, netloc):
        try:
            requests.get('https://' + netloc)
            return True
        except SSLError:
            return False
        except:
            return False
