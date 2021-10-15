import random

gesture_options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

class Human:
    def __init__(self):
        self.name = input('What is your name?: ')
        
    def choice(self):
        print(gesture_options)
        input('Which gesture do you choose?: ')

class AI:
    def __init__(self):
        self.name = 'Hal'

    def choice(self):
        random.choice(gesture_options)