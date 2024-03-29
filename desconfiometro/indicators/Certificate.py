import requests
from requests.exceptions import SSLError

from desconfiometro.indicators.BaseIndicator import BaseIndicator
from desconfiometro.blueprints.models.Result import Result


class Certificate(BaseIndicator):
    def __init__(self):
        pass

    def get_name(self):
        return "Certificados digitais"

    def get_description(self):
        return "Confere se o site possui certificados válidos. Um certificado digital é um arquivo eletrônico que serve como identidade virtual para uma pessoa física ou jurídica e auxilia na proteção nas trocas de informação."

    def get_type(self):
        return "boolean"

    def make_score(self, ok):
        return 10 if ok else 0

    def evaluate(self, parsed_url, registro_br):
        return self.has_valid_certificate(parsed_url.netloc)

    def has_valid_certificate(self, netloc):
        ok = None
        print("will get certificate")
        try:
            requests.get('https://' + netloc, timeout=3)
            ok = True
            print("ok")
        except SSLError:
            print("ssl error")
            ok = False
        except:
            print("exception")
            ok = None
        return None if (ok is None) else Result(self.get_name(), self.get_description(), self.make_score(ok),
                                                self.get_type())
