
from player import Player
from random import choice

gesture_options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

class AI:
    gesture_options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    def __init__(self):
        self.name = 'Hal'
        self.score = 0

    def ChooseAI(self, gesture_choice):
        self = None
