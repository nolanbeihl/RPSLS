gesture_options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

class Player:
    def __init__(self):
        self.name = input('What is your name?: ')

    def choice(self):
        print(gesture_options)
        self = input('Which gesture do you choose?: ')
        