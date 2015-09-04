from math import *
from random import random

NO_MOVE = 0
X = 1
O = 2

WINNING_STRUCTURES = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

def get_square(x):
    return floor(x/9.)

def get_box_in_square(x, square):
    return int(x + (square * 9))

def make_game_board():
    return [0 for i in range(81)]

def is_move_valid(game_board, move, prev_move):
    if move == -1:
        return False

    square          = get_square(prev_move)
    lower_bound     = square * 9
    higher_bound    = (square + 1) * 9
    
    if prev_move is -1 or (game_board[move] is NO_MOVE and (square_winner(game_board, square) is not NO_MOVE or (move < higher_bound and move >= lower_bound))):
        return True

    return False

def square_winner(game_board, square):
    for x in WINNING_STRUCTURES:
        box_0 = get_box_in_square(x[0], square)
        box_1 = get_box_in_square(x[1], square)
        box_2 = get_box_in_square(x[2], square)

        if game_board[box_0] == game_board[box_1] == game_board[box_2]:
            return game_board[box_0]

    return NO_MOVE

def game_over(game_board):
    for x in WINNING_STRUCTURES:
        s0 = square_winner(game_board, x[0])
        if s0 == square_winner(game_board, x[1]) == square_winner(game_board, x[2]) and s0 is not NO_MOVE:
            print ["GAME OVER", s0]
            return True

    return False

def make_move(game_board, player_id, player, prev_move):
    m = -1

    while is_move_valid(game_board, m, prev_move) is not True:
        m = player(game_board, prev_move)

    game_board[m] = player_id

    return m

def game_loop(players):
    game_board = make_game_board()
    move_counter = 0
    prev_move = -1

    while game_over(game_board) is False:
        for current_player in [0, 1]:
            prev_move = make_move(game_board, current_player + 1, players[current_player], prev_move)
            move_counter += 1

        print ["MOVE #", move_counter]
        print game_board

def print_game_board(game_board):
    return

stupid_player = lambda x, y: int(random()*81)

game_loop([stupid_player, stupid_player])
