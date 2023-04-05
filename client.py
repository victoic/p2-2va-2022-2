from window import Window
from file import FileReader, FileWriter
import os
from board import Board
from player import Player

dir = os.path.dirname(os.path.realpath(__file__))

class Client(Window):
    def __init__(self):
        if not os.path.exists(os.path.join(dir, 'logs', 'log_player1')):
            open(os.path.join(dir, 'logs', 'log_player1'), 'w').close()
            self.player_id = 0

            super().__init__(FileReader('logs', 'log_server'), FileWriter('logs', 'log_player1'))
        elif not os.path.exists(os.path.join(dir, 'logs', 'log_player2')):
            open(os.path.join(dir, 'logs', 'log_player2'), 'w').close()
            self.player_id = 1

            super().__init__(FileReader('logs', 'log_server'), FileWriter('logs', 'log_player2'))

        else:
            print('Both players are already connected')
            exit()

        self.player = Player(self.player_id)

        # Feito por Gustavo Henrique
        self.board = Board(10)

        contador = 0

        while contador != 10:
            size = int(input("insira o tamanho do navio "))
            posicao = [int(input("posicao x")), int(input("posicao y"))]
            orientacao = int(input("digite a orientacao 0 ( horizontal) 1 (vertical)"))
            self.board.placeShip(size, posicao, orientacao,self.player_id)
            contador += 1

        self.board.displayBoard()

    def _getLastLineTokens(self):
        lines = self.history.splitlines()
        last_line = lines[-1]
        tokens = last_line.split(' ')
        return tokens
    
    def _getOtherPlayerId(self):
        return (self.player_id + 1) % 2

    # Feito por Arthut Brandão
    def gameLoop(self):
        end_game = False
        while not end_game:
            changed = False

            while not changed:
                changed = self.checkAction()
                tokens = self._getLastLineTokens()

            if tokens[0] != 'SHOOT' or tokens[1] != str(self._getOtherPlayerId()):
                target = [int(tokens[2]), int(tokens[3])]
                self.board.reveal(target)
                self.writeAction(f'RESULT  {target[0]} {target[1]} {self.board.cells[target[0]][target[1]].get_symbol()}')
                self.board.shoot(target)

            if tokens[0] != 'START' or tokens[1] != str(self.player_id):
                row = input('Enter row to shoot')
                col = input('Enter col to shoot')
                target = self.player.shoot(row, col)
                self.writeAction(f'SHOOT {target[0]} {target[1]}')

            if tokens[0] != 'RESULT' or tokens[1] != str(self._getOtherPlayerId()):
                value = tokens[4]
                self.board.cells[int(tokens[2])][int(tokens[3])].symbol = value
            
    def writeAction(self, action):
        self.file_writer.operate(action)
    
if __name__ == '__main__':
    c1 = Client()
    c2 = Client()
    c3 = Client()