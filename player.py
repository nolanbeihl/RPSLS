gesture_options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

class Player:
<<<<<<< HEAD
    def __init__(self):
        self.name = input('')
=======
    def __init__(self, score):
        self.name = input('Please enter your name:')
>>>>>>> 40ad04afaea85c5174a3fee36e40d1b7cca6d89a
        self.score = 0

    def choice(self):
        print(gesture_options)
        self = input('Which gesture do you choose?: ')
