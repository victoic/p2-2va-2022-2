
class Board:
    def __init__(self, size):
        self.size = size
        self.letters = [chr(i) for i in range(65, 65 + size)]
        print(self.letters)
        # self.board = [[0 for i in range(size * 2)] for j in range(size)]


if __name__ == "__main__":
    board = Board(10)
