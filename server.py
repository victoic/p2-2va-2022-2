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

    def checkAction(self):
        if self.currentTurn == 1:
            file_content = self.file_reader_p1.operate()
        else:
            file_content = self.file_reader_p2.operate()
        if file_content != self.history[self.currentTurn]:
            self.history = file_content
            return True
        return False 

    def writeAction(self, action):
        self.server_writer.operate(action)

    def _getLastLineTokens(self):
        lines = self.history.splitlines()
        last_line = lines[-1]

        return last_line

    def gameLoop(self):
        while True:
            if self.checkAction():
                last_line = self._getLastLineTokens()
                
                self.writeAction(last_line)
                if self.currentTurn == 1:
                    self.currentTurn = 2
                else:
                    self.currentTurn = 1
    def checkCheating(self):
        actions_p1 = self.file_reader_p1.operate().splitLines()
        actions_p2 = self.file_reader_p2.operate().splitlines()
        history_p1 = self.history[1].splitlines()
        history_p2 = self.history[2].splitlines()

        cheat_p1 = all([action_history in actions_p1 for action_history in history_p1])
        cheat_p2 = all([action_history in actions_p2 for action_history in history_p2])
        return cheat_p1 and cheat_p2
