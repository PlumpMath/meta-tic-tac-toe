from math import *
from random import random

NO_MOVE = 0
X = 1
O = 2
char_chart = ["-", "X", "O"]

WINNING_STRUCTURES = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

def get_square(x):
    return int(floor(x/9.))

def get_box_number(x):
    return int(x - get_square(x)*9)

def get_box_in_square(x, square):
    return int(x + (square * 9))

def make_game_board():
    return [0 for i in range(81)]

def is_move_valid(game_board, move, prev_move):
    if move == -1:
        return False

    square          = get_box_number(prev_move)
    lower_bound     = square * 9
    higher_bound    = (square + 1) * 9
    
    if (prev_move is -1
    or (game_board[move] is NO_MOVE and square_winner(game_board, get_square(move)) is NO_MOVE and (square_winner(game_board, square) is not NO_MOVE or square_full(game_board, square) or (move < higher_bound and move >= lower_bound)))):
        return True

    return False

def square_full(game_board, square):
    full = True
    for i in range(9):
        full = full and game_board[get_box_in_square(i, square)] is not NO_MOVE

    return full

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
            print ["GAME OVER", char_chart[s0]]
            return True

    full = True
    for i in range(9):
        full = full and (square_full(game_board, i) or square_winner(game_board, i) is not NO_MOVE)

    if full is True:
        print ["GAME OVER", "TIE"]

    return full

def make_move(game_board, player_id, player, prev_move):
    m = -1
    move_counter = 0

    while is_move_valid(game_board, m, prev_move) is not True:
        m = player(game_board, prev_move)
        move_counter += 1
        if move_counter > 400:
            return -2

    if move_counter > 0:
        game_board[m] = player_id

    return m

def game_loop(players):
    game_board = make_game_board()
    move_counter = 0
    prev_move = -1

    while game_over(game_board) is False:
        for current_player in [0, 1]:
            prev_move = make_move(game_board, current_player + 1, players[current_player], prev_move)
            if prev_move >= 0:
                move_counter += 1
                print ["MOVE #", move_counter, "BY", char_chart[current_player + 1]]
                print_game_board(game_board)

def print_game_board(game_board):
    output = ""
    strings = ["","","","","","","","",""]
    line = 0
    end_char = " "

    for i in range(81):
        if i > 0:
            if i % 3 is 0:
                line += 1
            if i % 9 is 0:
                line -= 3
            if i % 27 is 0:
                line += 3
            if (i + 1) % 3 is 0:
                end_char = "  "
            else:
                end_char = " "
            


        strings[line] += char_chart[game_board[i]] + end_char

    for i, string in enumerate(strings):
        print string
        if (i - 2) % 3 is 0 and i > 0:
            print ""

stupid_player = lambda x, y: int(random()*81)
game_loop([stupid_player, stupid_player])
