class Cell():
    def __init__(self):
        self.symbol = "˜"
        self.hidden = True
        self.shot = False
    
    def getSymbol(self):
        if self.hidden == True:
            return '?'
        if self.shot == True:
            return 'X'
        return self.symbol
    
    def setSymbol(self, symbol):
        self.symbol = symbol

    def getHidden(self):
        return self.hidden

    def setHidden(self, hidden):
        self.hidden = hidden

    def getShot(self):
        return self.shot

    def setShot(self, shot):
        self.shot = shot