# caian 20/08/2015 
"""
Gomoku Game.
"""

from matrix import Matrix
from io import *

menu = {
	0 : 'exit',
	1 : 'Play!(just humans)'
}
# Size of matrix
SIZE = 5 

# Start menu.
def start_menu():
	for i in menu:
		print("%d : %s" % (i, menu[i]))
	return ask_num("Chose one!")

# Type of players
players = {
	0 : 'O',
	1 : 'X',
	2 : 'C'
}

# Turn function.
def turn(player, m):
	if player == players[2]:
		computer_turn()
		return
	r = m[(0,0):]
	print("Player %s, do your move(chose between 1 an %d, plz)" % (player, SIZE))
	col = ask_num("Chose a column")
	row = ask_num("Chose a row")
	r[row-1,col-1] = player
	return r

# Validate turn
def validate_turn():
	turn = ask("Is that your move?(\'s\' ou \'n\')")
	if turn == 's':
		return True
	return False 

# Play function.
def play():
	print("This is a Gomoku-game. Type your deserved option: ")
	option = start_menu()
	if option == 0:
		print("%s" % "bye!!")
		return
	m = Matrix(5,5,'+')
	rm = m[(0,0):]
	print("Let's play!")
	playing = True
	valid = False
	i = 0
	print(m)
	while playing:
		while not valid:
			rm = turn(players[0], m)
			print(rm)
			valid = validate_turn()
		m = rm
		valid = False
		while not valid:
			rm = turn(players[1], m)
			print(rm)
			valid = validate_turn()
		m = rm
		print(m)
		valid = False
		i = i + 1
		if i > 5:
			playing = False
	print("bye!! :D")

play()
