
class BaseIndicator():
    
    def __init__(self):
        pass
    
    def get_name(self):
        return "-"
        
    def get_description(self):
        return "-"

    def get_type(self):
        return "default"
    
    def evaluate(self, parsed_url):
        pass
