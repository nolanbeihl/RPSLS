from player import Player
from gameboard import Gameboards
Gameboards.competition()


class Compare():
    def __init__(self):
        self.compare = ''
    
    def comparison( player1_selection, player2_selection):
        
        
        
        if player1_selection.upper == 'ROCK':
            if player2_selection.upper == 'SCISSORS':
                print (f'{player1_selection.name} wins because rock crushes scissors')
                player1_selection.score += 1
            elif player2_selection.upper == 'PAPER':
                print (f'{player2.name} wins because paper covers rock.')
                player2.score += 1
            elif player2_selection.upper == 'SPOCK':
                print (f'{player2.name} wins because Spock vaporizes rock.')
                player2.score += 1
            elif player2_selection.upper == 'LIZARD':
                print (f'{player2.name} wins because lizard poisons Spock.')
                player2.score += 1
        
        if player1_selection.upper == 'PAPER':
            if player2_selection.upper == 'SCISSORS':
                print (f'{player2.name} wins because scissors cut paper.')
                player2.score += 1
            elif player2_selection.upper == 'ROCK':
                print (f'{player1_selection.name} wins because paper covers rock.')
                player1.score += 1
            elif player2.upper == 'SPOCK':
                print (f'{player1_selection.name} wins because paper disproves Spock.')
                player1.score += 1
            elif player2_selection.upper == 'LIZARD':
                print (f'{player2.name} wins because lizard eats paper.')
                player2.score += 1
        
        if player1_selection.upper == 'SCISSORS':
            if player2_selection.upper == 'PAPER':
                print (f'{player1_selection.name} wins because scissors cut paper.')
                player1.score +=1
            if player2.upper == 'ROCK':
                print(f'{player2.name} wins because rock crushes scissors.')
                player2.score +=1
            if player2_selection.upper == 'LIZARD':
                print (f'{player1_selection.name} wins because scissors decapitate lizard.')
                player1.score += 1
            if player2_selection.upper == 'SPOCK':
                print (f'{player2_selection.name} wins because Spock smashes scissors.')
                player2.score += 1

        if player1.upper == 'LIZARD':
            if player2.upper == 'ROCK':
                print(f'{player2.name} wins because Rock crushes Lizard')
                player2.score += 1
            elif player2.upper == 'PAPER':
                print(f'{player1.name} wins because Lizard eats Paper')
                player1.score += 1
            elif player2.upper == 'SCISSORS':
                print(f'{player2.name} wins because Scissors decapitates Lizard')
                player2.score += 1
            elif player2.upper == 'SPOCK':
                print(f'{player2.name} wins because Lizard poisons Spock')
                player2.score += 1
        if player1.upper == 'SPOCK':
            if player2.upper == 'ROCK':
                print(f'{player1.name} wins because Spock vaporized Rock')
                player1.score += 1
            elif player2.upper == 'PAPER':
                print(f'{player2.name} wins because Paper disproves Spock')
                player2.score += 1
            elif player2.upper == 'SCISSORS':
                print(f'{player1.name} wins because Spock smashes Scissors')
                player1.score += 1
            elif player2.upper == 'LIZARD':
                print(f'{player2.name} wins because Lizard poisons Spock')
                player2.score += 1
   