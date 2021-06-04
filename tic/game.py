from colorama import init
init(autoreset=True)

from colorama import Fore

from tic import Player, TicTacToe

class Game:

    def __init__(self):
        self.active = True
        self.player_one = Player("Player One")
        self.player_two = Player('Player Two')
        self.play = TicTacToe()

    def name_players(self):
        self.player_one.name = input('what is player one\'s name?\n>> ')
        self.player_two.name = input('what is player two\'s name?\n>> ')

    def get_player(self):
        turn = self.play.turn
        if turn == 0:
            return self.player_one
        if turn == 1:
            return self.player_two

    def show_player_score(self):
        print(Fore.CYAN + f'{self.player_one.name} has won {self.player_one.score} games, and {self.player_two.name} has won {self.player_two.score} games')

    def start(self):
        while self.active == True:
            player = self.get_player()
            self.play.show()
            move = input(f'{player.name}, which square would you like to place your token? 1-9\n>> ')

            if self.play.check_empty(move):
                continue
            move = int(move)
            
            if move < 1 or move > 9:
                self.play.error()
                continue

            self.play.place(move)
            self.play.taken_squares += 1

            if self.play.check_for_win_or_stalemate():
                self.play.show()
                if self.play.check_stale_mate():
                    self.play.reset_board()
                    self.play.change_turn()
                    break
                else:
                    player.score += 1
                    self.play.reset_board()
                    self.play.change_turn()
                    break

            self.play.change_turn()

    def game_loop(self):
        loops = 0
        while self.active == True:
            if loops < 1:
                response = input('do you want to play a game?\n>> ')
            else:
                self.show_player_score()
                response = input('do you want to play again?\n>> ')
            if response in ['yup', 'yes', 'y', 'sure', 'yeah']:
                if loops == 0:
                    self.name_players()
                    loops += 1
                self.start()
            else:
                print('okay, thanks for playing!')
                self.show_player_score()
                self.active = False


start = Game()
start.game_loop()