import requests
from requests.exceptions import SSLError

from desconfiometro.indicators.BaseIndicator import BaseIndicator
from desconfiometro.blueprints.models.Result import Result


class Certificate(BaseIndicator):

    def __init__(self):
        pass

    def get_name(self):
        return "Certificados"
        
    def get_description(self):
        return "Confere se possui certificados válidos"

    def get_type(self):
        return "boolean"

    def make_score(self, ok):
        return 10 if ok else 0

    def evaluate(self, parsed_url):
        return self.has_valid_certificate(parsed_url.netloc)

    def has_valid_certificate(self, netloc):
        ok = None
        print(netloc)
        try:
            requests.get('https://' + netloc, timeout = 3)
            ok = True
        except SSLError:
            ok = False
        except:
            ok = None


        return None if (ok == None) else Result(self.get_name(), self.get_description(), self.make_score(ok), self.get_type())
        