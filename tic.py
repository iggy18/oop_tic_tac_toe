from colorama import init
init(autoreset=True)

from colorama import Fore, Back, Style

class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0



class Square:

    def __init__(self, value=' '):
        self.value = value



class TicTacToe:

    def __init__(self):
        self.board = [[Square() for j in range(3)] for i in range(3)]
        self.turn = 0
        self.taken_squares = 0

    def show(self):
        sqr = self.board
        print(f'_{sqr[0][0].value}_|_{sqr[0][1].value}_|_{sqr[0][2].value}_')
        print(f'_{sqr[1][0].value}_|_{sqr[1][1].value}_|_{sqr[1][2].value}_')
        print(f' {sqr[2][0].value} | {sqr[2][1].value} | {sqr[2][2].value} ')

    def get_coordinates(self, input):
        positions = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
        move = positions[input-1]
        return move

    def nope(self):
        print(Fore.RED + 'that spot is already taken')

    def error(self):
        print(Fore.RED + 'the value must be a single integer')

    def change_turn(self):
            if self.turn == 0:
                self.turn = 1
            else:
                self.turn = 0

    def place(self, input):
        move = self.get_coordinates(input)
        if self.turn == 0:
            token = 'O'
        if self.turn == 1:
            token = 'X'
        if self.board[move[0]][move[1]].value == ' ':
            self.board[move[0]][move[1]].value = token
        else:
            self.nope()
            self.change_turn()

    def check_row_for_win(self):
        row = 0
        played = ['X', 'O']
        square = self.board
        for i in range(3):
            if square[row][0].value in played and square[row][0].value == square[row][1].value == square[row][2].value:
                return True
            row += 1
        return False


    def check_col_for_win(self):
        col = 0
        played = ['X', 'O']
        square = self.board
        for i in range(3):
            if square[0][col].value in played and square[0][col].value == square[1][col].value == square[2][col].value:
                return True
            col += 1
        return False

    def check_stale_mate(self):
        if self.taken_squares == 9:
            print(Fore.RED + 'This game has ended in a stalemate.')
            return True
        return False

    def check_for_win_or_stalemate(self):
        if self.check_col_for_win():
            print(Fore.GREEN + 'col win')
            return True
        if self.check_row_for_win():
            print(Fore.GREEN + 'row win')
            return True
        if self.check_stale_mate():
            print(Fore.GREEN + 'stale')
            return True
        else:
            return False

    def reset_board(self):
        for row in self.board:
            for col in row:
                col.value = ' '

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

    def start(self):
        while self.active == True:
            player = self.get_player()
            self.play.show()
            move = int(input(f'{player.name}, where would you like to move? 1-9\n>> '))
            
            if move < 1 > 9:
                self.play.error()
                self.play.change_turn()
            self.play.place(move)

            if self.play.check_for_win_or_stalemate():
                self.play.show()
                self.play.reset_board()
                self.play.change_turn()
                break

            self.play.change_turn()

    def game_loop(self):
        loops = 0
        while self.active == True:
            response = input('do you want to play a game?\n>> ')
            if response in ['yup', 'yes', 'y', 'sure', 'yeah']:
                if loops == 0:
                    self.name_players()
                    loops += 1
                self.start()
            else:
                self.active = False


start = Game()
start.game_loop()