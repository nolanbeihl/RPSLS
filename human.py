
from player import Player

gesture_options = ['1) Rock', '2) Paper', '3) Scissors', '4) Lizard', '5) Spock']

class Human(Player):
    def __init__(self):
        self.name = input('What is your name?: ')
        

