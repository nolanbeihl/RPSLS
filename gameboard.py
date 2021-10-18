

from random import random
from compare import Compare
from player import Player
from ai import AI
from compared import Compared
Player()
AI()
Compared()

class Gameboards:
    def __init__ (self):
        self.welcome = print("Welcome to the wonderful world of trying to reason with Sheldon. \n I don't have any idea why you are going to try, but good luck. \n Scenario: you are sitting in Sheldon's spot so he is obviously unhappy.\n In a rare act of reasonable behavior, he has challenged you to a game of Rock Paper Scissors Lizard Spock.\n What's that you say? You don't know the rules?  Great, now we get to listen to him explain them AGAIN! \n Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, \n Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, \n and as it always has, rock crushes scissors.")

    def competition():
        quantity = input ('How many players will there be, 1 or 2? ')
        gesture_options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

        if quantity == ('1'):
            print (gesture_options)
            player1= Player(0) 
            player2 = AI()
            print (f"So we have {player1.name} and {player2.name} competing for a spot on the couch today.  Well, let's get started.")
            while player1.score  < 2 and player2.score < 2:
                player1_selection = input (f'{player1.name} please make a selection based off the options given above. ')
                player2_selection = AI.choice(self=random.choice(gesture_options))
                Compare.comparison(player1_selection, player2_selection)
        

        if quantity == ('2'):
            print (gesture_options)
            player1= Player(0)
            player2= Player(0)
            print (f"So we have {player1.name} and {player2.name} competing for a spot on the couch.  Well, let's get started.")
            while player1.score  < 2 and player2.score < 2:
                
                player1_selection = input (f'{player1.name} please make a selection based off the options given above. ')
                player2_selection = input (f'{player2.name} please make a selection based off the options given above. ')
                if player1_selection == player2_selection:
                    print ('There are no winners or losers.  Sheldon, stop pouting.  You get to try again.')
                else:
                    Compare.comparison(player1_selection, player2_selection)
                
                    
                
                    

    
