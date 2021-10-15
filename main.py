from player import Player
from ai import AI

Player()
AI()

pick = ''
Player.choice(pick)

user_input = int(input('How many players are there today?: '))

if user_input == 2:
    player1 = Player()
    player2 = Player()
else:
    player1 = Player()
    player2 = AI()

gesture_options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

if user_input.upper != index(gesture_options).upper