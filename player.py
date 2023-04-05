import string

from board import Board
from ship import Ship


class Player():
    def __init__(self, board: Board, ships: list(Ship)):
        self.board = board
        self.ships = ships

    def shoot(row: int, column: str) -> bool:
        return self.board.shoot([row, string.ascii_uppercase.index(column.upper())+1])

    def __shipsPositions(self, ship: Ship) -> list(int[2]):
        if ship.orientation == 0:  # Horizontal
            return [(ship.position[0], ship.position[1] + i) for i in range(ship.size)]
        elif ship.orientation == 1:  # Vertical
            return [(ship.position[0] + i, ship.position[1]) for i in range(ship.size)]

    def hasShip(self, pos: int[2]):
        for ship in self.ships:
            if pos == self.__shipsPositions(ship):
                return True
        return False
