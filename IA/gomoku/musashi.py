# caian 02/09/2015
"""
Artificial Inteligence for the Gomoku game.
"""

from matrix import Matrix
from tree import Tree
from node import Node
import copy

class Musashi(object):
    """
    Musashi was a expert samurai who developed the techinique to fight with 2 swords. He was never defeated on combat.
    The main intention to name this as Musashi is the 'double threat' concept to win the game. 2 swords, 'double threat'.
    """
    
    """
    r = Node() # root
    t = Tree() # tree
    """
    def __init__(self, board, player):
        self.board = board
        self.ORIENTATION = ['H','V']
        # move sould be 'O' or 'X'
        self.PLAYER = player
    
    def domove(self, board):
        """
        The Main method to this AI. Returns a valid move to a given board.
        On my implementation, the board is represented as a 2D Matrix from the import, but could be
        whatever you want.
        """
        self.board = board
        move = self.choosemove() # return a list
        print("heuristic, row and col:",move[0], move[1], move[2])
        return move

    def choosemove(self):
        """
        Choose the best move on the value obtained by the calcvalue() method.
        The return of the function is a list containing the following:
            [best heuristic value, best row, best col]
        """
        # this line is to better code
        b = copy.deepcopy(self.board)
        # central point
        i = int(b.height / 2)
        j = int(b.width / 2) 
        # verity matrix
        vmatrix = Matrix(b.height, b.width, False)
        # heuristic value
        hvalue = 0
        bestvalue = -99999
        besti = i
        bestj = j
        # played?
        played = False
        for count in range(0, i+1):
            if count == 0:
                if b[i,j] == '+':
                    b[i,j] = self.PLAYER
                    hvalue = self.calcvalue(b, self.PLAYER)
                    played = True
                vmatrix[i,j] = True
            else:
                vm = vmatrix[(i-count,j-count):(i+1+count,j+1+count)]
                for row in range(0,vm.height):
                    for col in range(0,vm.width):
                        if vm[row,col] != True:
                            if b[i-count+row,j-count+col] == '+':
                                b[i-count+row,j-count+col] = self.PLAYER
                                hvalue = self.calcvalue(b, self.PLAYER)
                                played = True
                            vmatrix[i-count+row,j-count+col] = True
                            vm[row,col] = True
                        if played:
                            b[i-count+row,j-count+col] = '+'
                            if hvalue >= bestvalue:
                                bestvalue = hvalue
                                besti = i-count+row
                                bestj = j-count+col
                            played = False
                        # print(vmatrix)
                        # raw_input()
            if played:
                b[i,j] = '+'
                if hvalue >= bestvalue:
                    bestvalue = hvalue
                    besti = i
                    bestj = j
                played = False
        
        return [bestvalue, besti, bestj]

    def calcvalue(self, board, player):
        """
        Calculate the heuristic value to a given board.
        """
        # matrix of values
        values = Matrix(board.height, board.height, 0)
        value = 6

        for i in range(0, board.height):
            for j in range(0, board.width):
                if board[i,j] != '+':
                    if board[i,j] != player:
                        value = -value
                    # get row, col and diagonal to calculate values
                    self.addvaluesline(values, i, j, value, self.ORIENTATION[0])
                    self.addvaluesline(values, i, j, value, self.ORIENTATION[1])
                    # diagonals
                    self.addvaluesdline(values, i, j, value)
                    values[i,j] += value
                value = abs(value)
        # print(values)
        # raw_input()
        valuessum = 0
        for each in values:
            valuessum += each

        return valuessum

    def addvaluesdline(self, board, i, j, value):
        """
        Adds the value to the valueindes on the diagonal line of the board.
        Example:
            +1
              +2
                +3 ...(etc)
        IMPORTANT: Not add value to board[i,j]!!
        """
        index = i
        jndex = j
        # normal diagonal
        for spot in range(1, board.height*2):
            if spot % 2 == 0:
                index = index + spot
                jndex = jndex + spot
            else:
                index = index - spot
                jndex = jndex - spot
            if index in range(0, board.height) and jndex in range(0, board.width):
                correctvalue = abs(value)
                if abs(i - abs(index)) < 5:
                    correctvalue = correctvalue - abs(i - abs(index))
                else:
                    correctvalue = 1
                if value > 0:
                    board[index,jndex] += correctvalue
                else:
                    board[index,jndex] -= correctvalue 
        index = i
        jndex = j
        # inverse diagonal
        for spot in range(1, board.height*2):
            if spot % 2 == 0:
                index = index - spot
                jndex = jndex + spot
            else:
                index = index + spot
                jndex = jndex - spot
            if index in range(0, board.height) and jndex in range(0, board.width):
                correctvalue = abs(value)
                if abs(i - abs(index)) < 5:
                    correctvalue = correctvalue - abs(i - abs(index))
                else:
                    correctvalue = 1
                if value > 0:
                    board[index,jndex] += correctvalue
                else:
                    board[index,jndex] -= correctvalue
                    
    def addvaluesline(self, board, i, j, value, orientation):
        """
        Adds the value to the valueindex line and compensate on the line.
        Example:
            +1 +1 +2 +3 +4 +5 (value = +0) +5 +4 +3 +2 +1
            IMPORTANT: not add the value to the INDEX.
        """
        index = 0
        if orientation == self.ORIENTATION[0]: # horizontal
            index = i
        else:
            index = j

        for spot in range(1, board.height*2):
            if spot % 2 == 0:
                index = index + spot
            else:
                index = index - spot
            if index in range(0, board.height):
                correctvalue = abs(value)
                if orientation == self.ORIENTATION[0]: # horizontal
                    if abs(i - abs(index)) < 5:
                        correctvalue = correctvalue - abs(i - abs(index))
                    else:
                        correctvalue = 1
                if orientation == self.ORIENTATION[1]: # vertical
                    if abs(j - abs(index)) < 5:
                        correctvalue = correctvalue - abs(j - abs(index))
                    else:
                        correctvalue = 1
                if value > 0:
                    if orientation == self.ORIENTATION[0]: # horizontal
                        board[index,j] += correctvalue
                    else: # vertical
                        board[i,index] += correctvalue
                else:
                    if orientation == self.ORIENTATION[0]: # horizontal
                        board[index,j] -= correctvalue
                    else: # vertical
                        board[i,index] -= correctvalue
