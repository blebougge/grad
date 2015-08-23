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
SIZE = 15 
# Sequence to win a game
SEQUENCE = 5
# Max sequences of turns
MAX_TURNS = 20

# Directions to check: Horizontal, Vertical and Diagonal
directions = ['H','V','D']

# Start menu.
def start_menu():
	for option in menu:
		print("%d : %s" % (option, menu[option]))
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
	playable = False
	row = 0
	col = 0
	print("Player %s, do your move(chose between 1 an %d, plz)" % (player, SIZE))
	while not playable:
		row = ask_num("Chose a row")
		col = ask_num("Chose a column")
		if m[row-1,col-1] == '+':
			playable = True
		else:
			print("Sorry, chose another move!")
	r[row-1,col-1] = player
	return r

# Validate turn
def validate_turn():
	turn = ask("Is that your move?(\'s\' ou \'n\')")
	if turn == 's':
		return True
	return False 

# Check for a final state of the game
def is_over(m):
	r = False
	for direction in directions:
		r = (r or check_over(m, direction))
	return r

# Check if its over on one direction
def check_over(m, direction):
	print(direction)
	if direction == 'H':
		return iterate_over(m,'row')
	elif direction == 'V':
		return iterate_over(m,'col')
	elif direction == 'D':
		return False
	else:
		return False
	
# Iterate over a line to search a sequence of 5
def iterate_over(m, where):
	sequence = 0
	sym_list = []
	for line in range(0,SIZE):
		if where == 'row':
			sym_list = m.row(line)
		elif where == 'col':
			sym_list = m.col(line)
		else:
			return False
		#if sym_list[0] != '+':
		#	sequence += 1
		back_pos = 0
		for symbol in sym_list:
			if symbol != '+':
				if (symbol == sym_list[back_pos]):
					sequence += 1
				else:
					sequence = 0
			else:
				sequence = 0
			if sequence == SEQUENCE:
				return True
			back_pos += 1
		sequence = 0
	return False

# Play function.
def play():
	print("This is a Gomoku-game. Type your deserved option: ")
	option = start_menu()
	if option == 0:
		print("%s" % "bye!!")
		return
	m = Matrix(SIZE,SIZE,'+')
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
		if is_over(m):
			break
		valid = False
		while not valid:
			rm = turn(players[1], m)
			print(rm)
			valid = validate_turn()
		m = rm
		print(m)
		if is_over(m):
			break
		valid = False
		i = i + 1
		if i > MAX_TURNS:
			playing = False
	print("bye!! :D")

play()
