class Board:
    # Singleton
    _instance = None

    def __new__(cls, size):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.size = size
            cls._instance.board = [[Cell() for i in range(2 * size)] for j in range(size)]
            return cls._instance
        else:
            return Exception("Board already exists")

    
    def displayBoard(self):
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        print('  ', end='')
        for i in range(self.size): print(' ' + letters[i], end='')
        print('   ', end='')
        for i in range(self.size): print(' ' + letters[i], end='')
        print()
        for i in range(self.size):
            print(str(i + 1).rjust(2) + ' ', end='')
            for j in range(2 * self.size):
                if j == self.size: print('   ', end='')
                cell = self.board[i][j]
                symbol = cell.getSymbol()
                print(symbol, end=' ')
            print()
