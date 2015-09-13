# caian 20/08/2015 
"""
Gomoku Model.
"""

from matrix import Matrix
from musashi import Musashi

# Sequence to win a game
SEQUENCE = 5
# Directions to check: Horizontal, Vertical and Diagonal
directions = ['H','V','D']

class Gomoku(object):

    COMPUTER = 'C'

    def __init__(self, size, empty_spot):
        self.size = size
        self.empty_spot = empty_spot
        self.m = Matrix(self.size, self.size, self.empty_spot)
        self.musashi = Musashi(self.m, self.COMPUTER)

    # Check for a spot to be placed a move
    def check_spot(self, row, col):
        return self.m[row,col] == self.empty_spot

    # Do the move
    def do_move(self, row, col, player):
        self.m[row,col] = player
        return self.copy_matrix()
    
    # Copy the matrix
    def copy_matrix(self):
        return self.m[(0,0):]

    # Show the matrix
    def show_matrix(self):
        return str(self.m)
        
    # TODO: Computer turn
    def computer_turn(self):
        comp_move = self.musashi.domove(self.m)
        return self.do_move(comp_move[0], comp_move[1], self.COMPUTER) 
        
    # Check for a final state of the game
    def is_over(self):
        r = False
        for direction in directions:
            r = (r or self.check_over(direction))
        return r

    # Check if its over on one direction
    def check_over(self, direction):
        # mes(direction)
        if direction == 'H':
            return self.iterate_over('row')
        elif direction == 'V':
            return self.iterate_over('col')
        elif direction == 'D':
            return self.iterate_diagonal()
        else:
            return False
	
    # Iterate over a line to search a sequence of 5
    def iterate_over(self, where):
        sequence = 0
        sym_list = []
        for line in range(0,self.size):
            if where == 'row':
                sym_list = self.m.row(line)
            elif where == 'col':
                sym_list = self.m.col(line)
            else:
                return False
            back_pos = 0
            for symbol in sym_list:
                if symbol != self.empty_spot:
                    if symbol == sym_list[back_pos]:
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
    
    # Iterate over the diagonals to search a sequence of 5
    def iterate_diagonal(self):
        sequence = 0
        sym_list = []
        for diagonal in range(-29,30):
            back_pos = 0
            sym_list = self.m.diagonal(diagonal)
            for symbol in sym_list:
                if symbol != self.empty_spot:
                    if symbol == sym_list[back_pos]:
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
    
