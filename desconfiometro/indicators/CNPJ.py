from desconfiometro.indicators.BaseIndicator import BaseIndicator
from desconfiometro.blueprints.models.Result import Result
from desconfiometro.indicators.utils import get_registro_br
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import re
import json


class CNPJ(BaseIndicator):
    def __init__(self):
        self.filename = "desconfiometro/indicators/data/cnpj/cnpj.txt"

    def get_name(self):
        return "CNPJ"

    def get_description(self):
        return "Confere se a empresa por trás do link possui CNPJ e seu respectivo status"

    def get_type(self):
        return "cnpj"

    def make_score(self, state):
        return 10 if state == "Ativa" else 0

    def evaluate(self, parsed_url, registro_br):
        with open(self.filename, "r") as f:
            reg_cnpj = registro_br["entities"][0]["publicIds"][0]["identifier"]
            line = f.readline()
            while line:
                list = line.split(',')
                cnpj = list[0].strip()
                if cnpj == reg_cnpj:
                    name = list[1].strip()
                    state = list[2].strip()
                    r = Result(self.get_name(), self.get_description(), self.make_score(state), self.get_type())
                    r.data = (name, state)
                    return r
                line = f.readline()

