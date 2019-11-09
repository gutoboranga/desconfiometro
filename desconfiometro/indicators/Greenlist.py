from desconfiometro.indicators.BaseIndicator import BaseIndicator


class Greenlist(BaseIndicator):

    def __init__(self):
        self.file = open('desconfiometro/indicators/data/greenlist.txt')

    def get_name(self):
        return "Greenlist"

    def get_type(self):
        return "boolean"

    def evaluate(self, parsed_url):
        return self.is_greenlisted(parsed_url.netloc)

    def is_greenlisted(self, item):
        line = self.file.readline()
        while line:
            if line.strip() == item:
                return True
            line = self.file.readline()
        return False
