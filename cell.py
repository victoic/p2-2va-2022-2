class Cell():
    def __init__(self, symbol):
        self.symbol = symbol
        self.hidden = True
        self.shot = False
    
    def getSymbol():
        if self.hidden == True:
            return '?'
        if self.shot == True:
            return 'X'         
        return self.symbol