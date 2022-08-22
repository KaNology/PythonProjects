import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def getmove(self, game):
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
                if val not in game.spots:
                    raise ValueError
                valid_spot = True
            except ValueError:
                print('Invalid Spot. Try again!')
        return val

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        spot = random.choice(game.spots)
        return spot