class Color:
    EMPTY = 0
    WHITE = 1
    BLACK = 2

class Empty:
    color = Color.EMPTY

    def get_moves(self, board, x, y):
        raise Exception('Error! here is no any figure!')

    def __str__(self):
        return ' '

class ChessMan: # common figure class
    IMG = None

    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __str__(self):
        return self.IMG[0 if self.color == Color.WHITE else 1]

    def get_color(self):
        return self.color

class Pawn(ChessMan):
    IMG = ('♟', '♙')

    def get_moves(self, board, y, x):
        moves = [[y, x]]
        if self.color == Color.WHITE:
            if y < 7 and board.get_color(x, y+1) != self.color:
                moves.append([y-1, x])
            else:
                return 1
        else:
            if y > 0 and board.get_color(x, y+1) != self.color:
                moves.append([y+1, x])
            else:
                return 1
        return moves


class King(ChessMan):
    IMG = ('♚', '♔')

    def get_moves(self, board, x, y):
        moves = []
        return moves

class Queen(ChessMan):
    IMG = ('♛', '♕')

    def get_moves(self, board, x, y):
        pass

class Rock(ChessMan):
    IMG = ('♜', '♖')

    def get_moves(self, board, x, y):
        pass

class Knight(ChessMan):
    IMG = ('♞', '♘')

    def get_moves(self, board, x, y):
        pass

class Bishop(ChessMan):
    IMG = ('♝', '♗')

    def get_moves(self, board, x, y):
        pass
