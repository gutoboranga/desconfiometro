from desconfiometro.indicators.BaseIndicator import BaseIndicator


class SpecialCharacters(BaseIndicator):

    def __init__(self):
        self.special_chars = ['-']

    def get_name(self):
        return "SpecialCharacters"

    def get_type(self):
        return "boolean"

    def evaluate(self, parsed_url):
        if any(x in parsed_url.netloc for x in self.special_chars):
            return True
        else:
            return False
