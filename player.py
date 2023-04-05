import string

class Player():
    def __init__(self, id: int, board: Board, ships: list(Ship)):
        self.id = id
        self.board = board
        self.ships = []

    def shoot(letter: int, number: int):
        coord = input("Escreva a letra e o número (coordenada) correspondente à posição que você quer atacar: ")
        letter_number = coord.split(" ")
        letter = letter_number[0].upper()
        number = int(letter_number[1])
        return self.board.shoot(ord(letter)-64, number)

    def hasShip(self, pos: int[2]):
        for ship in self.ships:
            if pos == self.__shipsPositions(ship):
                return True
        return False

    def __shipsPositions(self, ship: Ship) -> list(int[2]):
        if ship.orientation == 0:  # Horizontal
            return [(ship.position[0], ship.position[1] + i) for i in range(ship.size)]
        elif ship.orientation == 1:  # Vertical
            return [(ship.position[0] + i, ship.position[1]) for i in range(ship.size)]
