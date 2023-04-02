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

    def print_board(self, hide_ships):
        print('  | ' + ' | '.join([chr(i+65) for i in range(self.size)]) + ' |')
        print('--+' + '+'.join(['--' for i in range(self.size)]) + '--')
        for i in range(self.size):
            row = []
            for j in range(self.size):
                if self.board[i][j] == 's' and hide_ships:
                    row.append(' ')
                else:
                    row.append(self.board[i][j])
            print(str(i+1).rjust(2) + '| ' + ' | '.join(row) + ' |')

    def is_valid_coord(self, row, col):
        return row >= 0 and row < self.size and col >= 0 and col < self.size

    def is_hit(self, row, col):
        for ship in self.ships:
            if (row, col) in ship.coords:
                ship.hit()
                self.board[row][col] = 'X'
                return True
        self.board[row][col] = '-'
        return False

class Ship:
    def __init__(self, size):
        self.size = size
        self.coords = []
        self.hits = 0

    def generate_coords(self, board):
        while True:
            direction = random.choice(['h', 'v'])
            if direction == 'h':
                row = random.randint(0, board.size-1)
                col = random.randint(0, board.size-self.size)
                coords = [(row, col+i) for i in range(self.size)]
            else:
                row = random.randint(0, board.size-self.size)

   

    