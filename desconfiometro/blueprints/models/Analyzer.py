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
        
        for weighted_indicator in self.weighted_indicators:
            indicator = weighted_indicator[0]
            weight = weighted_indicator[1]
            
            result = indicator.evaluate(url)
            
            print(result)
            
            if result != None:
                newResults.append(result)
                newScore += result.value * weight
                validWeightsSum += weight
            
        self.results = newResults
        self.score = self.score = round(newScore / validWeightsSum, 2)
        
        if self.score > 10.0:
            self.scope = 10.0

