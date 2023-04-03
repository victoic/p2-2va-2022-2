
class Board:
    def __init__(self, size):
        self.size = size
        self.boardA = [chr(i) for i in range(65, 65 + size)]
        self.boardB = [chr(i) for i in range(65, 65 + size)]
        # self.board = [[0 for i in range(size * 2)] for j in range(size)]

    def displayBoard(self):
        print(self.boardA, " | ", self.boardB)
        

if __name__ == "__main__":
    board = Board(10)
    board.displayBoard()
