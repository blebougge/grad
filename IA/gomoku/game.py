# caian 31/08/2015
"""
Gomoku Game.
"""

from gomoku import Gomoku
from io import *

menu = {
    0 : 'exit',
    1 : 'Play!(just humans)',
    2 : 'Human vs Computer(Not avaliable)'
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
    while not playable:
        row = ask_num("Chose a row")
        col = ask_num("Chose a column")
        if gomoku.check_spot(row-1,col-1):
            playable = True
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
    elif option == 2:
        mes("Sorry, not avaliable :(")
        return
    elif option != 1:
        mes("Not valid option!")
        return
    rm = gomoku_game.copy_matrix()
    mes("Let's play!")
    playing = True
    valid = False
    i = 0
    mes(gomoku_game.show_matrix())
    while playing:
        while not valid:
            rm = turn(players[0], gomoku_game)
            mes(rm)
            valid = validate_turn()
        if gomoku_game.is_over():
            break
        mes(gomoku_game.show_matrix())
        valid = False
        while not valid:
            rm = turn(players[1], gomoku_game)
            mes(rm)
            valid = validate_turn()
        if gomoku_game.is_over():
            break
        mes(gomoku_game.show_matrix())
        valid = False
        i = i + 1
        if i > 20:
            playing = False
    mes("bye!! :D")

play()
