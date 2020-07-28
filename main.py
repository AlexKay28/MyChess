from board import *
from figures import *

b = Board()
print(b.start_position())
print(b.board[6][3])
print(b.get_color(6, 3))
print(b.get_moves(6, 3))
moves = b.get_moves(6, 3)
b.move(moves[0], moves[1])
print(b)
