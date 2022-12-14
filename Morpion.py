import random

class Game:

    def __init__(self):
        self.board = []

    #On va créer un plateau de jeu de 3x3
    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    #Le programme choisi le joueur qui commencera 
    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    #
    def is_player_win(self, player):
        win = None

        n = len(self.board)

        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Au tour du joueur {player}")

            self.show_board()

            row, col = list(
                map(int, input("Entrez la ligne et la colonne où placer votre pion : ").split()))
            print()

            self.fix_spot(row - 1, col - 1, player)

            if self.is_player_win(player):
                print(f"Le joueur {player} Gagne la partie !")
                break

            if self.is_board_filled():
                print("Égalité !")
                break

            player = self.swap_player_turn(player)

        print()
        self.show_board()


game = Game()
game.start()

