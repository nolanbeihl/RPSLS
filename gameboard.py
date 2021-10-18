

from random import choice
#from compare import Compare
from player import Player
from ai import AI


class Gameboards:
    

    def __init__ (self):
        self.welcome = print("Welcome to the wonderful world of trying to reason with Sheldon. \n I don't have any idea why you are going to try, but good luck. \n Scenario: you are sitting in Sheldon's spot so he is obviously unhappy.\n In a rare act of reasonable behavior, he has challenged you to a game of Rock Paper Scissors Lizard Spock.\n What's that you say? You don't know the rules?  Great, now we get to listen to him explain them AGAIN! \n Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, \n Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, \n and as it always has, rock crushes scissors.")
        self.player1 = None
        self.player2 = None
        self.playerAI = None

    # class Compare():
    # def __init__(self):
    #     self.compare = ''
        
    def comparison( self, player1_selection, player2_selection, ):
        player1_score = 0
        player2_score = 0
        
        # while player1_score < (2) and player2_score < (2):
            
        
        if player1_selection.upper()  == ('ROCK'):
            if player2_selection.upper() == ('SCISSORS'):
                print (f'{self.player1.name} wins because rock crushes scissors')
                self.player1.score += 1
            elif player2_selection.upper() == ('PAPER'):
                print (f'{self.player2.name} wins because paper covers rock.')
                self.player2.score += 1
                
                

            elif player2_selection.upper() == ('SPOCK'):
                print (f'{self.player2.name} wins because Spock vaporizes rock.')
                self.player2.score += 1
            else:
                    #player2_selection.upper == 'LIZARD':
                print (f'{self.player2.name} wins because lizard poisons Spock.')
                self.player2.score += 1

        if player1_selection.upper() == ('PAPER'):
            if player2_selection.upper == ('SCISSORS'):
                print (f'{self.player2.name} wins because scissors cut paper.')
                self.player2.score += 1
            elif player2_selection.upper() == ('ROCK'):
                print (f'{self.player1.name} wins because paper covers rock.')
                self.player1.score += 1
            elif player2_selection.upper() == ('SPOCK'):
                print (f'{self.player1.name} wins because paper disproves Spock.')
                self.player1.score += 1
            else:
                # player2_selection.upper() == 'LIZARD':
                print (f'{self.player2.name} wins because lizard eats paper.')
                self.player2.score += 1

        if player1_selection.upper() == ('SCISSORS'):

            if player2_selection.upper() == ('PAPER'):
                print (f'{self.player1.name} wins because scissors cut paper.')
                self.player1.score +=1
            elif player2_selection.upper() == ('ROCK'):
                print(f'{self.player2.name} wins because rock crushes scissors.')
                self.player2.score +=1
            elif player2_selection.upper() == ('LIZARD'):
                print (f'{self.player1.name} wins because scissors decapitate lizard.')
                self.player1.score += 1
            else:
                # player2_selection.upper() == 'SPOCK':
                print (f'{self.player2.name} wins because Spock smashes scissors.')
                self.player2.score += 1

        if player1_selection.upper() == ('LIZARD'):
            if player2_selection.upper() == ('ROCK'):
                print(f'{self.player2.name} wins because Rock crushes Lizard')
                self.player2.score += 1
            elif player2_selection.upper() == ('PAPER'):
                print(f'{self.player1.name} wins because Lizard eats Paper')
                self.player1.score += 1
            elif player2_selection.upper() == ('SCISSORS'):
                print(f'{self.player2.name} wins because Scissors decapitates Lizard')
                self.player2.score += 1
            else:
                # player2.upper() == 'SPOCK':
                print(f'{self.player2.name} wins because Lizard poisons Spock')
                self.player2.score += 1
        if player1_selection.upper() == ('SPOCK'):
            if player2_selection.upper() == ('ROCK'):
                print(f'{self.player1.name} wins because Spock vaporized Rock')
                self.player1.score += 1
            elif player2_selection.upper() == ('PAPER'):
                print(f'{self.player2.name} wins because Paper disproves Spock')
                self.player2.score += 1
            elif player2_selection.upper() == ('SCISSORS'):
                print(f'{self.player1.name} wins because Spock smashes Scissors')
                self.player1.score += 1
            else:
                # player2.upper() == 'LIZARD':
                print(f'{self.player2.name} wins because Lizard poisons Spock')
                self.player2.score += 1

    def competition(self):
        
        player1_score = 0
        player2_score = 0
        quantity = input ('How many players will there be, 1 or 2? ')
        gesture_options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

        

        if quantity == ('1'):
            print (gesture_options)
            self.player1= Player(0) 
            self.player2 = AI()
            print (f"So we have {self.player1.name} and {self.player2.name} competing for a spot on the couch today.  Well, let's get started.")
            while self.player1.score < 2 and self.player2.score < 2:
                player1_selection = input (f'{self.player1.name} please make a selection based off the options given above. ')
                player2_selection = self.player2(ai_choice = choice(gesture_options))
                self.comparison(player1_selection, player2_selection)
        

        if quantity == ('2'):
            print (gesture_options)
            self.player1= Player(0)
            self.player2= Player(0)
            print (f"So we have {self.player1.name} and {self.player2.name} competing for a spot on the couch.  Well, let's get started.")
            # while player1_score  < 2 and player2_score < 2:
            while self.player1.score < (2) and self.player2.score < (2): 
                player1_selection = input (f'{self.player1.name} please make a selection based off the options given above. ')
                player2_selection = input (f'{self.player2.name} please make a selection based off the options given above. ')
                if player1_selection == player2_selection:
                    print ('There are no winners or losers.  Sheldon, stop pouting.  You get to try again.')
                    
                else:
                    
                    self.comparison(player1_selection, player2_selection)
                
        if self.player1.score == 2:
            print (f'{self.player1.name} won.  They get the couch.')
        if self.player2.score == 2:
            print (f'{self.player2.name} won.  THey get the couch.')
                    
                
                    
                
                    

    
