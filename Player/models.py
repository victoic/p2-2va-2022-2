class Player():
    def __init__(self, board: Board, ships: list(Ship)):
        self.board = board
        self.ships = []

    def shoot(pos: tuple(int, int)):
        pass

    def hasShip(self, pos: tuple(int, int)):
        for ship in self.ships:
            if pos == self.__shipsPositions(ship):
                return True
        return False

    def __shipsPositions(self, ship: Ship) -> list(tuple(int, int)):
        if ship.orientation == 0:  # Horizontal
            return [(ship.position[0], ship.position[1] + i) for i in range(ship.size)]
        elif ship.orientation == 1:  # Vertical
            return [(ship.position[0] + i, ship.position[1]) for i in range(ship.size)]
