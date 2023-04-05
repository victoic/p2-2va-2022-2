from cell import Cell 

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

    
    def displayBoard(self, playerId = 0):
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        print('  ', end='')
        for i in range(self.size): print(' ' + letters[i], end='')
        print('   ', end='')
        for i in range(self.size): print(' ' + letters[i], end='')
        print()
        if playerId == 0:
            for i in range(self.size):
                print(str(i + 1).rjust(2) + ' ', end='')
                for j in range(2 * self.size):
                    if j == self.size: print('   ', end='')
                    cell = self.board[i][j]
                    symbol = cell.getSymbol()
                    print(symbol, end=' ')
                print()
                
        elif playerId == 1:
            for i in range(self.size):
                print(str(i + 1).rjust(2) + ' ', end='')
                for j in range(self.size, 2 * self.size):
                    if j == 2 * self.size - 1: print('   ', end='')
                    cell = self.board[i][j]
                    symbol = cell.getSymbol()
                    print(symbol, end=' ')

                for k in range(self.size - 1):
                    if k == self.size: print('   ', end='')
                    cell = self.board[i][j]
                    symbol = cell.getSymbol()
                    print(symbol, end=' ')
                print()

    def reveal(self, pos):
        row, col = pos
        cell = self.board[row - 1][col + self.size - 1]
        if not cell.hidden: return "Already revealed"
        cell.hidden = False

    def shoot(self, pos):
        row, col = pos
        cell = self.board[row - 1][col - 1]
        if cell.shot: return "Already shot"
        cell.shot = True


    def placeShip(self, size, pos, orientation, playerId):
        row, col = pos
        if playerId == 1: col += self.size
        for i in range(size):
            if orientation == 0: cell = self.board[row][col + i]
            elif orientation == 1: cell = self.board[row + i][col]
            cell.symbol = "="

if __name__ == "__main__":
    board = Board(10)
    board.placeShip(3, (0, 0), 0, 0)
    board.placeShip(3, (0, 0), 1, 1)
    board.reveal((1, 1))
    board.shoot((1, 1))
    board.shoot((1, 2))
    board.shoot((1, 3))
    board.displayBoard(1)
