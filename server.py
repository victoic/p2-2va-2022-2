from window import Window

class Server(Window):
    __instance = None

    def __init__(self):
        self.__currentTurn = 1
        self.__log_writer = FileWriter(os.path.join(dir, '../log'), 'log_server.txt')
        self.__p1_writer = FileWriter(os.path.join(dir, '../log'), 'log_player1.txt')
        self.__p2_writer = FileWriter(os.path.join(dir, '../log'), 'log_player2.txt')
        super().__init__()

    def __new__(cls):
        if not hasattr(cls, '__instance'):
            cls.__instance = super(Server, cls).__new__(cls)
        return cls.__instance

    def resetFiles(self):
        self.__log_writer.operate("", "w")
        self.__p1_writer.operate("", "w")
        self.__p2_writer.operate("", "w")

    def checkCheating(self):
        pass
    
    def checkAction(self):
        pass

    def writeAction(self):
        pass

    def gameLoop(self):
        pass