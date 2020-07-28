from figures import *

class Board:
    def __init__(self):
        # FORMAT (char - y, numbers - x): example: e2 = [6, 3], e4 = [4 , 3]
        self.board = [[Empty()] * 8 for y in range(8)]
        self.letters = 'a b c d e f g h'.split(' ')
        self.letters.reverse()
        print(self.letters)

    def start_position(self):

        # pawns
        for x in range(8):
            self.board[1][x] = Pawn(Color.BLACK, 1)
            self.board[6][x] = Pawn(Color.WHITE, 1)

        # kings
        self.board[7][4] = King(Color.WHITE, 100)
        self.board[0][4] = King(Color.BLACK, 100)

        # rocks
        self.board[0][0] = Rock(Color.BLACK, 5)
        self.board[0][7] = Rock(Color.BLACK, 5)
        self.board[7][0] = Rock(Color.WHITE, 5)
        self.board[7][7] = Rock(Color.WHITE, 5)

        # Queens
        self.board[0][3] = Queen(Color.BLACK, 6)
        self.board[7][3] = Queen(Color.WHITE, 6)

        # Knights
        self.board[0][2] = Knight(Color.BLACK, 3)
        self.board[0][5] = Knight(Color.BLACK, 3)
        self.board[7][2] = Knight(Color.WHITE, 3)
        self.board[7][5] = Knight(Color.WHITE, 3)

        #Bishops
        self.board[0][1] = Bishop(Color.BLACK, 3)
        self.board[0][6] = Bishop(Color.BLACK, 3)
        self.board[7][1] = Bishop(Color.WHITE, 3)
        self.board[7][6] = Bishop(Color.WHITE, 3)

    def get_color(self, x, y):
        return self.board[x][y].color

    def get_moves(self, y, x):
        return self.board[y][x].get_moves(self, y, x)

    def move(self, xy_from, xy_to):
        self.board[xy_to[0]][xy_to[1]] = self.board[xy_from[0]][xy_from[1]]
        self.board[xy_from[0]][xy_from[1]] = Empty()

    def __str__(self):
        res = ''
        c = 0
        for y in range(8):
            for x in range(8):

                res += f'\u001b[4{c + 3};m'
                res += '  ' + str(self.board[y][x]) + '\t'
                c = 1 - c
            res += '\u001b[0m \t' + str(8 - y) + '\n'
            c = 1 - c
        res += '\u001b[0m' + '\t'.join(self.letters)
        return res


if __name__ == "__main__":
    b = Board()
    print(b.start_position())
    print(b.board[6][3])
    print(b.get_color(6, 3))
    print(b.get_moves(6, 3))
    moves = b.get_moves(6, 3)
    b.move(moves[0], moves[1])
    print(b)
