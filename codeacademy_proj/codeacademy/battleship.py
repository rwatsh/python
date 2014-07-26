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

ship_row = random_row(board)
ship_col = random_col(board)

print ship_row
print ship_col

# Player has 4 turns to guess right or else the game is over.
for turn in range(4):
    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Col: "))

    if guess_row not in range(5) or guess_col not in range(5):
            print "Oops, that's not even in the ocean."
    elif board[guess_row][guess_col] == "X":
            print "You guessed that one already."
    else:
        if guess_row == ship_row and guess_col == ship_col:
            print "Congratulations! You sank my battleship!"
            break
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = 'X'
            print "Turn", turn + 1
            print_board(board)
    if turn == 3:
            print "Game Over"



