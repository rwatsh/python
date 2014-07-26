__author__ = 'rushil'
"""
Battleship game.

Build a simplified, one-player version of the classic board game Battleship! In this version of the game,
there will be a single ship hidden in a random location on a 5x5 grid. The player will have 10
guesses to try to sink the ship.
"""
from random import randint

# Create a 5x5 matrix viz. list of 5 lists of 5 'O's
board = []
for i in range(0, 5):
    lst = []
    for j in range(0, 5):
        lst.append('O')
    board.append(lst)

def print_board(board):
    for row in board:
        """
            Calling join() on string to connect all elements
            in the row list with " "
        """
        print " ".join(row)

print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board) - 1)

random_row(board)
random_col(board)

