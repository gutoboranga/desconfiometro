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
        
        for indicator in self.weighted_indicators:
            r = indicator[0].evaluate(url)
            w = indicator[1]
            
            if r != None:
                newResults.append(r)
                
                if r.type == 'boolean':
                    w = w * 10
                
                newScore += r.value * w
            
        self.results = newResults
        self.score = newScore
