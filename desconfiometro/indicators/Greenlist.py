from desconfiometro.indicators.BaseIndicator import BaseIndicator
from desconfiometro.blueprints.models.Result import Result

class Greenlist(BaseIndicator):

    def __init__(self):
        self.filename = 'desconfiometro/indicators/data/greenlist.txt'

    def get_name(self):
        return "Lista dos confirmados"
        
    def get_description(self):
        return "Confere se é um dos confirmados"

    def get_type(self):
        return "boolean"
        
    def make_score(self, ok):
        return 10 if ok else 0

    def evaluate(self, parsed_url):
        return self.is_greenlisted(parsed_url.netloc)

    def is_greenlisted(self, item):
        ok = False
        
        with open(self.filename) as f:
            line = f.readline()

            while line:
                if line.strip() == item:
                    ok = True
                    break
                line = f.readline()
                
        return Result(self.get_name(), self.get_description(), self.make_score(ok), self.get_type())
