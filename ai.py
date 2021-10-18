
from player import Player
import random

gesture_options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

class AI:
    gesture_options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    def __init__(self):
        self.name = 'Hal'
        self.score = 0

    def choice(self):
        #self.ai_choice
        ai_choice = random.choice(gesture_options)
        print(f'Hal chose {ai_choice}')
