from player import Player
import random

gesture_options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

class AI(Player):
    def __init__(self):
        self.name = 'Hal'
        self.score = 0

    def choice(self):
        self = random.choice(gesture_options)
        print(f'Hal chose {self}')
