gesture_options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

class Player:
    def __init__(self, score):
        self.name = input ('Enter your name please')
        self.score = 0

    def choice(self):
        print(gesture_options)
        self = input('Which gesture do you choose?: ')
