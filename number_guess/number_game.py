import random

class GuessingGame:

    def __init__(self, difficulty='easy'):
        self.score = 0
        self.guesses_left = 0
        self.guesses = 0
        self.mode = difficulty
        self.hints = False
        self.number = 0

    def set_difficulty_level(self):
        if self.mode == 'easy':
            self.number = random.randint(1,10)
            self.guesses_left = 5
        if self.mode == 'medium':
            self.number = random.randint(1,20)
            self.guesses_left = 6
        if self.mode == 'hard':
            self.number = random.randint(1,50)
            self.guesses_left = 7

    def get_hint(self, guess):
        if guess < self.number:
            print('try a higher number!\n')
        if guess > self.number:
            print('try a lower number\n')

    def enable_hints(self, answer):
        if answer == 'yes':
            self.hints = True

    def check_for_win(self, guess):
        if self.number == guess:
            print(f'\nyou guessed it! the number was {self.number}!\n')
            self.score += 1
            return True
        else:
            print('\nguess again.\n')
            if self.hints == True:
                self.get_hint(guess)


class PlayGame:

    def __init__(self):
        self.player_name = ''
        self.active = True
        self.game = GuessingGame()

    def set_up_game(self):
        print('before I can play with thee answer me these questions three...\n\n\n')

        self.player_name = input('what is your name?\n>>>')

        difficulty = input('\non a scale of "easy", "medium", "hard", how difficult would you like this to be?\n>>>')

        hints = input('\nwould you like hint a after an incorrect guess?\n>>>')

        if difficulty == 'medium':
            self.game.enable_hints(hints)
            self.game.mode = 'medium'
            self.game.set_difficulty_level()

        if difficulty == 'hard':
            self.game.enable_hints(hints)
            self.game.mode = 'hard'
            self.game.set_difficulty_level()

        else:
            self.game.enable_hints(hints)
            self.game.set_difficulty_level()


    def get_difficulty(self):
        mode = self.game.mode
        spread = {'easy': '1 - 10', 'medium': '1 - 20', 'hard':'1 - 50'}
        current_mode = spread.get(mode)
        return current_mode

    def game_loop(self):
        game = self.game

        self.set_up_game()

        mode = self.get_difficulty()

        print(f'welcome {self.player_name}! your game difficulty is set to {game.mode}! hints: {game.hints}, you have {game.guesses_left} guesses left\n')

        while game.guesses_left != 0 == False:
            number_guess = int(input(f'guess a number between {mode}\n>>>'))
            if self.game.check_for_win(number_guess):
                break
            self.game.guesses_left -= 1
            if self.game.guesses_left == 0:
                print('game over. you\'ve run out of guesses.\n')
            else:
                print(f'you have {self.game.guesses_left} guesses left\n')  
        

    def start_game(self):
        while self.active:
            answer = input('would you like to play a guessing game?\n>>>')
            if answer == 'yes':
                self.game_loop()
            else:
                self.active == False
        



game = PlayGame()
game.start_game()
