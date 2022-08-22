from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self, board_size, win_condition):
        self.winner = None
        self.board_size = board_size
        self.board = self.make_board(board_size)
        self.win_condition = win_condition
        self.spots = self.available_spots(board_size)

    @staticmethod
    def make_board(board_size):
        return [[' ' for _ in range(board_size)] for _ in range(board_size)]

    @staticmethod
    def available_spots(board_size):
        out = []
        for r in range(board_size):
            for c in range(board_size):
                out.append((r, c))
        return out

    # Print the current state of the board
    def print_board(self):
        count = 0
        idx = [str(i) for i in range(self.board_size)]
        print("      " + "   ".join(idx))
        print("---------------------------------------------")
        for row in range(self.board_size):
            r = [str(self.board[row][col]) for col in range(self.board_size)]
            print(str(count) + "   | " + " | ".join(r) + " |")
            count += 1

    # Check if there are any available spots left
    def empty_spots(self):
        return any(' ' in sublist for sublist in self.board)

    # Check if there is a winner. This will be checked after each move made.
    def is_winner(self, player, row, col):
        check_row = self.board[row][max(0, col - (self.win_condition - 1)) : min(self.board_size, col + self.win_condition)]
        for i in range(len(check_row) - (self.win_condition - 1)):
            sublist = check_row[i:i+self.win_condition]
            print(sublist)
            if all([s == player for s in sublist]):
                return True

        check_col = [self.board[r][col] for r in range(max(0, row - (self.win_condition - 1)), min(self.board_size, row + self.win_condition))]
        for i in range(len(check_col) - (self.win_condition - 1)):
            sublist = check_col[i:i+self.win_condition]
            if all([s == player for s in sublist]):
                return True

        diagonal1 = []

        for i in range(-self.win_condition + 1, self.win_condition):
            if row + i >= self.board_size or row + i < 0 or col + i >= self.board_size or col + i < 0:
                continue 
            diagonal1 += self.board[row + i][col + i]

        for i in range(len(diagonal1) - (self.win_condition - 1)):
            sublist = diagonal1[i:i+self.win_condition]
            if all([s == player for s in sublist]):
                return True

        diagonal2 = []

        for i in range(-self.win_condition + 1, self.win_condition):
            if row - i >= self.board_size or row - i < 0 or col + i >= self.board_size or col + i < 0:
                continue 
            diagonal2 += self.board[row - i][col + i]

        for i in range(len(diagonal2) - (self.win_condition - 1)):
            sublist = diagonal2[i:i+self.win_condition]
            if all([s == player for s in sublist]):
                return True

        return False

    # Make a move on the board
    # player: can be X or O
    # spot: the position the letter is placed
    # Return True if move is successfully made.
    def make_move(self, player, row, col):
        if(self.board[row][col] == ' '):
            self.spots.remove((row, col))
            self.board[row][col] = player
            if self.is_winner(player, row, col):
                self.winner = player
            return True
        return False

def play():
    board = TicTacToe(5, 3)
    player1 = HumanPlayer('X')
    player2 = RandomComputerPlayer('O')

    board.print_board()
    letter = 'X' # First player is X

    while board.empty_spots():
        if letter == 'X':
            spot = player1.get_move(board)
        else:
            spot = player2.get_move(board)

        if board.make_move(letter, spot[0], spot[1]):
            board.print_board()

            if board.winner:
                print(f"Player {board.winner} wins!")
                return None

            letter = 'O' if letter == 'X' else 'X'

    print("It's a tie!")

play()