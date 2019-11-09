from desconfiometro.indicators.BaseIndicator import BaseIndicator
from desconfiometro.blueprints.models.Result import Result


class SpecialCharacters(BaseIndicator):

    def __init__(self):
        self.special_chars = ['-']

    def get_name(self):
        return "Caracteres especiais"
        
    def get_description(self):
        return "Confere se tem - e etc bla bla"

    def get_type(self):
        return "boolean"

    def evaluate(self, parsed_url):
        ok = not self.contains_special_characters(parsed_url.netloc)
        return Result(self.get_name(), self.get_description(), (1 if ok else 0), self.get_type())

    def contains_special_characters(self, netloc):
        if any(x in netloc for x in self.special_chars):
            return True
        else:
            return False
