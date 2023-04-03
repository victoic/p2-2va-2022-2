class Cell():
    def __init__(self, symbolValue):
        self.symbol = symbolValue
        self.hidden = True
        self.shot = False
    
    def getSymbol():
        if self.hidden == True:
            return '?'
        if self.shot == True:
            return 'X'         
        return self.symbol