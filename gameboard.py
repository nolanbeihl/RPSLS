

from player import Player
from ai import AI

player1= Player()
player2= Player()
player3 = AI()


class gameboards:
    def __init__ (self):
        self.welcome = print("Welcome to the wonderful world of trying to reason with Sheldon. \n don't have any idea why you are going to try, but good luck. \n Scenario: you are sitting in Sheldon's spot so he is obviously unhappy.\n In a rare act of reasonable behavior, he has challenged you to a game of Rock Paper Scissors Lizard Spock.\n What's that you say? You don't know the rules?  Great, now we get to listen to him explain them AGAIN! \n Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, \n Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, \n and as it always has, rock crushes scissors.")

    def competition(self):
        quantity = input ('How many players will there be, 1 or 2? ')
        gesture_options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        print (gesture_options)
        if quantity == 1:
            pass

        if quantity == 2:
            while player1 < 2 and player2 < 2:
                pass
