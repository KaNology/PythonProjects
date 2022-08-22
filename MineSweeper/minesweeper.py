import random

class MinesweeperBoard:
    def __init__(self, dim_size, bombs_num):
        self.dim_size = dim_size
        self.bombs_num = bombs_num
        self.board = self.create_board()

        # Initialize the dug set. Keep track of the set of locations we have dug
        self.dug = set()

    # Initialize the board and plant bombs in random locations on the board
    def create_board(self):
        board = [[None for i in range(self.dim_size)] for i in range(self.dim_size)]

        # Plant the bombs
        bombs_planted = 0
        while bombs_planted < self.bombs_num:
            location = random.randint(0, self.dim_size ** 2 - 1)
            row = location // self.dim_size
            col = location % self.dim_size

            if board[row][col] == '*':
                continue
            board[row][col] = '*'
            bombs_planted += 1

        return board

    # Assign numbers to each spot on the board. This can be the way to determine how many adjacent bombs a spot has.
    def assign_numbers_on_board(self):
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if self.board[row][col] == '*':
                    continue
                
                self.board[row][col] = self.get_num_of_adjacent_bombs(row, col)

    # Get the number of adjacent bombs of a location on the board.
    def get_num_of_adjacent_bombs(self, row, col):
        # left: row, col - 1
        # top: row - 1, col
        # right: row, col + 1
        # bottom: row + 1, col
        # left, top: row - 1, col - 1
        # right, top: row - 1, col + 1
        # left, bottom: row + 1, col - 1
        # right, bottom: row + 1, col + 1
        num_of_bombs = 0
        
        for r in range(max(0, row - 1), min(self.dim_size - 1, row + 1) + 1):
            for c in range(max(0, col - 1), min(self.dim_size - 1, col + 1) + 1):
                if r == row and c == col:
                    continue

                if self.board[r][c] == '*':
                    num_of_bombs += 1
        
        return num_of_bombs

    # Player will dig one specific spots.
    # Returns: True if bomb is dug
    def dig(self, row, col):
        # Check if spot is already dug
        if (row, col) in self.dug:
            print("Spot is already dug, you dumb dumb!")
            return False
        
        self.dug.add((row, col))

        if self.board[row][col] == '*':
            return True

        if self.board[row][col] > 0:
            return False

        # If there is no bomb around the spot, then automatically dig that spot
        if self.board[row][col] == 0:
            for r in range(max(0, row - 1), min(self.dim_size - 1, row + 1) + 1):
                for c in range(max(0, col - 1), min(self.dim_size - 1, col + 1) + 1):
                    if (r, c) in self.dug:
                        continue

                    self.dig(r, c)

        return False

    # Returns number of undug spots
    def num_undug(self):
        return self.dim_size ** 2 - len(self.dug)

    def print_board(self):
        count = 0
        idx = [str(i) for i in range(self.dim_size)]
        print("      " + "   ".join(idx))
        print("---------------------------------------------")
        for row in range(self.dim_size):
            row = [str(self.board[row][col]) if (row, col) in self.dug else ' ' for col in range(self.dim_size)]
            print(str(count) + "   | " + " | ".join(row) + " |")
            count += 1

def play(dim_size = 10, bombs_num = 10):
    board = MinesweeperBoard(dim_size, bombs_num)
    board.assign_numbers_on_board()

    bomb_dug = False
    while not bomb_dug and board.num_undug() > bombs_num:
        board.print_board()
        row, col = map(int, input("Where do you want to dig? ").split())
        bomb_dug = board.dig(row, col)

    board.print_board()
    if bomb_dug:
        print("Booooooooom! You lost!")
        return bomb_dug

    print("Lucky this time... You win!")

play(5, 5)