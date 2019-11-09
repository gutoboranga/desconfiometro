import requests
from requests.exceptions import SSLError
from desconfiometro.indicators.BaseIndicator import BaseIndicator

class Certificate(BaseIndicator):

    def __init__(self):
        pass

    def get_name(self):
        return "Certificados"
        
    def get_description(self):
        return "Confere se possui certificados válidos"

    def get_type(self):
        return "boolean"

    def evaluate(self, parsed_url):
        return self.has_valid_certificate(parsed_url.netloc)

    def has_valid_certificate(self, netloc):
        ok = False
        
        try:
            requests.get('https://' + netloc, timeout = 2)
            ok = True
        except SSLError:
            ok = False
        except:
            ok = False

        return Result(self.get_name(), self.get_description(), (1 if ok else 0), self.get_type())