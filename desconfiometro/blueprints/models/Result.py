class Result():
    
    def __init__(self):
        self.indicator_name = ""
        self.indicator_description = ""
        self.value = ""
        self.type = ""
        self.data = ""
    
    def __init__(self, indicator_name, indicator_description, value, type):
        self.indicator_name = indicator_name
        self.indicator_description = indicator_description
        self.value = value
        self.type = type
        self.data = ""
        