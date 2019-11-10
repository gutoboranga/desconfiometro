from desconfiometro.indicators.ReclameAqui import ReclameAqui
from desconfiometro.indicators.Votes import Votes
from desconfiometro.indicators.DNS import DNS
from desconfiometro.blueprints.models.Result import Result
from desconfiometro.indicators.utils import get_registro_br


class Analyzer():
    
    def __init__(self, weighted_indicators):
        self.weighted_indicators = weighted_indicators
        self.results = []
        self.score = 0.0
    
    def getResults(self):
        return self.results
        
    def getScore(self):
        return self.score
    
    def run(self, url):
        newResults = []
        newScore = 0.0
        validWeightsSum = 0.0

        registro_br = get_registro_br(url.netloc)
        
        for weighted_indicator in self.weighted_indicators:
            indicator = weighted_indicator[0]
            weight = weighted_indicator[1]
            
            result = indicator.evaluate(url, registro_br)
            
            if result != None:
                newScore += result.value * weight
                validWeightsSum += weight
                
                if indicator.get_name() == Votes().get_name():
                    newResults.insert(0, result)
                elif indicator.get_name() == ReclameAqui().get_name():
                    newResults.insert(0, result)
                else:
                    newResults.append(result)

            elif indicator.get_name() == ReclameAqui().get_name():
                r = Result(indicator.get_name(), "O link pesquisado não foi encontrado no ReclameAqui. Para um e-commerce isto pode ser um mau indicativo.", 0, 'boolean')
                
                newResults.append(r)
                newScore += 0
                validWeightsSum += weight
                
            elif indicator.get_name() == DNS().get_name():
                
                r = Result(indicator.get_name(), "O endereço do link inserido não é registrado no Brasil", 0, 'boolean')
                
                newResults = [r]

                newScore = 0
                validWeightsSum = 1
                break
        
        self.results = newResults
        self.score = self.score = round(newScore / validWeightsSum, 2)
        
        if self.score > 10.0:
            self.scope = 10.0

