from player import Player
import random

gesture_options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

class AI(Player):
    def __init__(self):
        self.name = 'Hal'

    def choice(self):
        self = random.choice(gesture_options)