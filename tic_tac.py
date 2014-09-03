"""
Simple Tic-Tac-Toe game
"""


class Board(object):
    class Space(object):
        """
        Container class for the individual cells on the board
        """
        def __init__(self):
            # The cell contents need to be fixed width for the board to print
            # hence initializing with a blank space
            self.contains = " "

        def __str__(self):
            return self.contains

        def set(self, mark):
            self.contains = mark

        def is_empty(self):
            return self.contains == " "

        def __eq__(self, other):
            """For equality purposes empty cells are never equal,
            even when both cells are empty"""
            if not self.is_empty():
                return self.contains == other.contains
            else:
                return False

    def __init__(self):
        self.board = [[Board.Space(), Board.Space(), Board.Space()],
                      [Board.Space(), Board.Space(), Board.Space()],
                      [Board.Space(), Board.Space(), Board.Space()]]

    def get(self, x, y):
        return self.board[y][x]

    def submit_move(self, x, y, mark):
        if self.valid_move(x, y):
            self.board[y][x].set(mark)
            return True
        else:
            return False

    def valid_move(self, x, y):
        return self.board[y][x].is_empty()

    def __str__(self):
        return """
          0   1   2
       0  {0} | {1} | {2}
         ---+---+---
       1  {3} | {4} | {5}
         ---+---+---
       2  {6} | {7} | {8}
         """.format(
            self.board[0][0], self.board[0][1], self.board[0][2],
            self.board[1][0], self.board[1][1], self.board[1][2],
            self.board[2][0], self.board[2][1], self.board[2][2])


class Player(object):
    def __init__(self, mark):
        self.mark = mark
        self.game = None

    def make_move(self, x, y):
        self.game.play_move(self, x, y)


class Game(object):
    def __init__(self):
        self.board = Board()
        self.x_player = Player("X")
        self.x_player.game = self
        self.o_player = Player("O")
        self.o_player.game = self
        self.x_move = True
        self.game_finished = False
        self.winner = None

    def __str__(self):
        return str(self.board)

    def play_move(self, player, x, y):
        if (not self.game_finished) and self.board.submit_move(x, y, player.mark):
            print(str(self))
            self.test_finished()
        else:
            print(str(self))
            print("\nSpace is already taken, please choose another move")

    def get(self, x, y):
        return self.board.get(x, y)

    def test_finished(self):
        """Test all possible winning combinations, as well as
        whether the game ended in a draw"""
        for i in range(3):
            if (self.get(0, i) == self.get(1, i) == self.get(2, i) or
                    self.get(i, 0) == self.get(i, 1) == self.get(i, 2)):
                self.game_finished = True
                self.winner = self.get(i, i)
                return True
        if (self.get(0, 0) == self.get(1, 1) == self.get(2, 2) or
                self.get(2, 0) == self.get(1, 1) == self.get(0, 2)):
            self.game_finished = True
            self.winner = self.get(1, 1)
            return True
        full = True
        for row in self.board.board:
            for cell in row:
                if cell.is_empty():
                    full = False
        if full:
            self.game_finished = True
        if self.game_finished:
                if self.winner is not None:
                    print("\nThe game is over. The winner is {0}".format(self.winner))
                else:
                    print("\nCat's eye")
        return False

    def move_input(self):
        x = int(input("Input X coordinate\n"))
        y = int(input("Input Y coordinate\n"))
        return (x, y)

    def start_game(self):
        print(self)
        while not self.game_finished:
            if self.x_move:
                print("X's turn to play:\n")
                move = self.move_input()
                self.x_player.make_move(move[0], move[1])
                self.x_move = False
            else:
                print("O's turn to play:\n")
                move = self.move_input()
                self.o_player.make_move(move[0], move[1])
                self.x_move = True

def tic_tac_main():
    g = Game()
    g.start_game()
