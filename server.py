from window import Window

class Server(Window):
    __instance = None

    def __init__(self):
        self.__currentTurn = 0
        super().__init__()

    def __new__(cls):
        if not hasattr(cls, '__instance'):
            cls.__instance = super(Server, cls).__new__(cls)
        return cls.__instance

    def resetFiles(self):
        pass

    def checkCheating(self):
        pass
    
    def checkAction(self):
        pass

    def writeAction(self):
        pass

    def gameLoop(self):
        pass