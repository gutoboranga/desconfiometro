from desconfiometro.indicators.BaseIndicator import BaseIndicator
import requests


class WebOfTrust(BaseIndicator):

    def __init__(self):      
        pass

    def get_name(self):
        return "Web of Trust"

    def evaluate(self, parsed_url, registro_br):
        return self.classify_url(parsed_url.netloc)

    def classify_url(self, item):
        item

        line = self.file.readline()
        while line:
            if line.strip() == item:
                return True
            line = self.file.readline()
        return False
