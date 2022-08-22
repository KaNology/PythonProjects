import random
import math

class Player:
    def __init__(self, letter):
        self.letter = letter

    def getmove(self, board):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_spot = False
        val = None
        while not valid_spot:
            row, col = map(int, input(self.letter + "\'s turn. Input move: ").split())
            try:
                val = (row, col)
                if val not in game.available_spots():
                    raise ValueError
                valid_spot = True
            except ValueError:
                print('Invalid Spot. Try again!')
        return val

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        spot = random.choice(game.available_spots())
        return spot

class SuperSmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, board):
        if board.available_spots() == board.board_size ** 2:
            spot = random.choice(board.available_spots())
        else:
            spot = self.minimax(board, self.letter)['position']
        return spot

    def minimax(self, state, player):
        max_player = self.letter # The computer itself
        other_player = 'O' if player == 'X' else 'X' # The computer's imaginary opponent
        # So basically the computer is considering all possible states vs it's opponent then pick the best state to move

        # The base case (either player is a winner): check if the previous move is a winner move
        if state.winner:
            return {
                'position': None , 
                'score': 1 * (len(state.available_spots()) + 1) if state.winner == max_player else -1 * (len(state.available_spots()) + 1)
            }

        elif not state.empty_spots(): # No empty spots left (it's a tie)
            return {'position': None, 'score': 0}

        # Initialize the dictionaries
        if player == max_player:
            bestMove = {'position': None, 'score': -math.inf}
        else:
            bestMove = {'position': None, 'score': math.inf}

        for possibleMove in state.available_spots():
            # Make the move
            state.make_move(player, possibleMove[0], possibleMove[1])

            # Simulate an imaginary game against the other player
            simulationScore = self.minimax(state, other_player)

            # Undo the move
            state.board[possibleMove[0]][possibleMove[1]] = ' '
            state.winner = None
            simulationScore['position'] = possibleMove

            # Update the dictionaries if the move is indeed better
            if player == max_player:
                if simulationScore['score'] > bestMove['score']:
                    bestMove = simulationScore
            else:
                if simulationScore['score'] < bestMove['score']:
                    bestMove = simulationScore
        
        return bestMove