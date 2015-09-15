# caian 31/08/2015
"""
Gomoku Game.
"""

from gomoku import Gomoku
from io import *

menu = {
    0 : 'exit',
    1 : 'Play!(just humans)',
    2 : 'Human vs Computer',
    3 : 'Computer vs Human'
}
# Size of matrix
SIZE = 15 
# Max sequences of turns
MAX_TURNS = 20

# Start menu.
def start_menu():
	for option in menu:
		mes("%d : %s" % (option, menu[option]))
	return ask_num("Chose one!")

# Type of players
players = {
    0 : 'O',
    1 : 'X',
    2 : 'C'
}

# Turn function.
def turn(player, gomoku):
    if player == players[2]:
        return gomoku.computer_turn()
    playable = False
    row = 0
    col = 0
    mes("Player %s, do your move(chose between 1 an %d, plz)" % (player, SIZE))
    m = gomoku.copy_matrix()
    while not playable:
        row = ask_num("Chose a row")
        col = ask_num("Chose a column")
        if gomoku.check_spot(row-1,col-1):
            playable = True
            m[row-1,col-1] = player
            mes(m)
            if not validate_turn():
                playable = False
                m[row-1,col-1] = '+'
        else:
            mes("Sorry, chose another move!")
    return gomoku.do_move(row-1,col-1,player)

# Validate turn
def validate_turn():
    turn = ask("Is that your move?(\'y\' or \'n\')")
    if turn == 'y':
        return True
    return False 

# Play function.
def play():
    mes("This is a Gomoku-game. Type your deserved option: ")
    gomoku_game = Gomoku(SIZE, '+')
    option = start_menu()
    if option == 0:
        mes("bye!!")
        return
    elif option > 3:
        mes("Sorry, not avaliable :(")
        return
    elif option < 0:
        mes("Not valid option!")
        return
    rm = gomoku_game.copy_matrix()
    mes("Let's play!")
    playing = True
    valid = False
    i = 0
    mes(gomoku_game.show_matrix())
    while playing:
        if option == 1: # human vs human
            rm = turn(players[0], gomoku_game)
            if gomoku_game.is_over():
                break
            mes(gomoku_game.show_matrix())
            valid = False
            rm = turn(players[1], gomoku_game)
            if gomoku_game.is_over():
                break
            mes(gomoku_game.show_matrix())
            valid = False
        elif option == 2: # human vs computer
            rm = turn(players[0], gomoku_game)
            if gomoku_game.is_over():
                break
            mes(gomoku_game.show_matrix())
            valid = False
            rm = gomoku_game.computer_turn()
            mes("Computer turn:")
            mes(rm)
            if gomoku_game.is_over():
                break
        else: # computer vs human
            rm = gomoku_game.computer_turn()
            mes("Computer turn:")
            mes(rm)
            if gomoku_game.is_over():
                break
            rm = turn(players[0], gomoku_game)
            if gomoku_game.is_over():
                break
            mes(gomoku_game.show_matrix())
            valid = False
        i = i + 1
        if i > 30:
            playing = False
    mes("bye!! :D")

play()
