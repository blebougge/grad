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

"""
Start menu.
"""
def start_menu():
	for i in menu:
		print("%d : %s" % (i, menu[i]))
	return ask_num("Chose one!")

"""
Fill matrix function
"""
def init_m(m):
	for i in range(5):
		for j in range(5):
			m.__setitem__(tuple((i,j)),'+') 
	print(m)

"""
Play function.
"""
def play():
	print("This is a Gomoku-game. Type your deserved option: ")
	option = start_menu()
	if option == 0:
		print("%s" % "bye!!")
		return
	playing = True
	m = Matrix(5,5)
	init_m(m)
	while(playing):
		print("Let's play!")
		col = ask_num("Chose a column")
		row = ask_num("Chose a row")
		m.__setitem__(tuple((row-1,col-1)), 'O')
		print(m)
		playing = False

play()
