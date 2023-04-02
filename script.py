import random

class Board:
    def __init__(self, size):
        self.size = size
        self.ships = []
        self.board = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(' ')
            self.board.append(row)

    def add_ship(self, ship):
        self.ships.append(ship)
        for coord in ship.coords:
            row, col = coord
            self.board[row][col] = 's'

   

    