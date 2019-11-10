from desconfiometro.indicators.BaseIndicator import BaseIndicator
from desconfiometro.blueprints.models.Result import Result
from desconfiometro.indicators.utils import get_registro_br
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import re


class CNPJ(BaseIndicator):
    def __init__(self):
        self.file = open("cnpj.txt", "r")

    def get_name(self):
        return "CNPJ"

    def get_description(self):
        return "Confere se a empresa por trás do link possui CNPJ e seu respectivo status"

    def get_type(self):
        return "boolean"

    def make_score(self, ok):
        return 10 if ok else 0

    def evaluate(self, parsed_url, registro_br):
        line = self.file.readline()
        while line:

            list = line.split(',')
            cnpj = list[0].strip()


