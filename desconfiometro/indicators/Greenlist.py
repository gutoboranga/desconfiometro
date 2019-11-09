from desconfiometro.indicators.BaseIndicator import BaseIndicator


class Greenlist(BaseIndicator):

    def __init__(self):
        self.file = open('desconfiometro/indicators/data/greenlist.txt')

    def get_name(self):
        return "Greenlist"

    def evaluate(self, parsed_url):
        return self.contains(parsed_url.netloc)

    def contains(self, item):
        line = self.file.readline()
        while line:
            if line.strip() == item:
                return True
            line = self.file.readline()
        return False
