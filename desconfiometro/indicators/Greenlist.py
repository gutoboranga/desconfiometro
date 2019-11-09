from desconfiometro.indicators.BaseIndicator import BaseIndicator


class Greenlist(BaseIndicator):

    def __init__(self):
        self.file = open('desconfiometro/indicators/data/greenlist.txt')

    def get_name(self):
        return "Lista dos confirmados"
        
    def get_description(self):
        return "Confere se é um dos confirmados"

    def get_type(self):
        return "boolean"

    def evaluate(self, parsed_url):
        return self.is_greenlisted(parsed_url.netloc)

    def is_greenlisted(self, item):
        line = self.file.readline()
        ok = False
        
        while line:
            if line.strip() == item:
                ok = True
            line = self.file.readline()
        
        return Result(self.get_name(), self.get_description(), (1 if ok else 0), self.get_type())
