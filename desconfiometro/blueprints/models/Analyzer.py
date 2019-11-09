class Analyzer():
    
    def __init__(self, url, indicators):
        self.url = url
        self.indicators_list = indicators
        
    def run(self):
        results = []
        
        for indicator in self.indicators_list:
            r = indicator.evaluate(url)
            
            if r != none:
                results.append(r)
            
        return results