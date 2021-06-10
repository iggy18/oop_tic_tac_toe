import random
from words import words



class Hangman:

    def __init__(self):
        self.word = random.choice(words)
        self.display = ['_' for letter in self.word]
        self.guesses = 0


    def show(self):
        display = ' '.join(self.display)
        print(f'the word is: {display}')


    def get_word_index(self, guess):
        locations = []
        for index, char in enumerate(list(self.word)):
            if char == guess:
                locations.append(index)
        return locations


    def update(self, idx, letter):
        for number in idx:
            self.display[number] = letter


    def check_guess(self, guess):
        if guess in self.word:
            idx = self.get_word_index(guess)
            self.update(idx, guess)

    def check_for_win(self):
        display = ''.join(self.display)
        word = self.word
        if display == word:
            print('You Win!!!')
            return True
    

def game():
    word = Hangman()
    while True:
        guess = input('guess a letter\n>>> ')
        word.check_guess(guess)
        word.show()
        word.guesses += 1
        if word.check_for_win():
            print(f'you\'ve won in {word.guesses} guesses!')
            break

def loop():
    while True:
        response = input('Do you want to play a game?')
        if response == 'no':
            break
        game()

loop()