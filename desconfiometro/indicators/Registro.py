from desconfiometro.indicators.BaseIndicator import BaseIndicator
import requests


class Registro(BaseIndicator):

    def __init__(self):      
        pass

    def get_name(self):
        return "Registro do Domínio"

    def evaluate(self, parsed_url):
        return self.classify_url(parsed_url.netloc)
    
    def classify_url(self, item):
        
        url_request = "https://rdap.registro.br/domain/" + item
        print("request")
        try:
            req = requests.get(url = url_request, timeout=2)
        except SSLError:
            ok = False
        except:
            ok = False
        
        
        return None # Result(self.get_name(), self.get_description(), (1 if ok else 0), self.get_type())
