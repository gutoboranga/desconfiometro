class Analyzer():
    def __init__(self, indicators):
        self.indicators_list = indicators
        
    def run(self, url):
        results = []
        
        for indicator in self.indicators_list:
            r = indicator.evaluate(url)
            
            if r != None:
                results.append(r)
            
        return results