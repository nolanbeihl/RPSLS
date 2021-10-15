from player import Player

gesture_options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

class Human(Player):
    def __init__(self):
        self.name = input('What is your name?: ')
        