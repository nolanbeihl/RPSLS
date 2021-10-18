class Compared():
    def __init__(self):
        self.compare = ''
    
    def comparison(player1, player2):
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
      
            
