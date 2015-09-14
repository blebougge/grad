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
        # the 'working' function is here, above. Just remove the comment lines
        """
        self.board = board
        move = self.choosemove(self.board) # return a list
        # print("heuristic, row and col:",move[0], move[1], move[2])
        return [move[1], move[2]]
        """
        # here is where I'll be developing the best way to select.
        self.board = board
        listmove = self.choosemove(self.board) # return a list
        # best move!!
        bestmove = [ listmove[0], listmove[1], listmove[2] ]
        enemyboard = copy.deepcopy(board)
        # prevent next move list
        nextlistmove = []
        # now we find the best move for the enemy
        # enemy list move
        elistmove = []
        for each in listmove[3]:
            if board[each[0],each[1]] == '+':
                enemyboard[each[0],each[1]] = self.PLAYER
                elistmove = self.choosemove(enemyboard, 'O')
                print('each:',each)
                # find the next best move
                for eachone in elistmove[3]:
                    if enemyboard[eachone[0],eachone[1]] == '+':
                        enemyboard[eachone[0],eachone[1]] = 'O'
                        nextlistmove = self.choosemove(enemyboard)
                        """
                        Uncoment this line to see working!
                        print(enemyboard)
                        print(nextlistmove)
                        """
                        if nextlistmove[0] > bestmove[0]:
                            bestmove[0] = nextlistmove[0] # the heuristic value get up.
                            bestmove[1] = each[0] # better row
                            bestmove[2] = each[1] # better col
                            print('eachone:',eachone)
                            print(bestmove)
                        enemyboard[eachone[0],eachone[1]] = '+'
                enemyboard[each[0],each[1]] = '+'
                # print(enemyboard)
                # print(board)

        return [ bestmove[1], bestmove[2] ] 

    def choosemove(self, board, player=None):
        """
        Choose the best move on the value obtained by the calcvalue() method.
        The return of the function is a list containing the following:
            [best heuristic value, best row, best col, [board list] ]

        The [board list] is the list of the possible moves. This will be used
        in the following select of the best sequence of moves. (ps: still on develop)
        """
        if player == None:
            p = self.PLAYER
        else:
            p = player
        # this line is to better code
        b = copy.deepcopy(board)
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
        # moves list
        moves = []
        for count in range(0, i+1):
            if count == 0:
                if b[i,j] == '+':
                    b[i,j] = p
                    hvalue = self.calcvalue(b, p)
                    played = True
                    # moves append
                    moves.append((i,j))
                vmatrix[i,j] = True
                if played:
                    b[i,j] = '+'
                    if hvalue >= bestvalue:
                        bestvalue = hvalue
                        besti = i
                        bestj = j
                    played = False
            else:
                vm = vmatrix[(i-count,j-count):(i+1+count,j+1+count)]
                for row in range(0,vm.height):
                    for col in range(0,vm.width):
                        if vm[row,col] != True:
                            if b[i-count+row,j-count+col] == '+':
                                b[i-count+row,j-count+col] = p
                                hvalue = self.calcvalue(b, p)
                                played = True
                            vmatrix[i-count+row,j-count+col] = True
                            vm[row,col] = True
                            # moves append
                            moves.append((i-count+row,j-count+col))
                        if played:
                            b[i-count+row,j-count+col] = '+'
                            if hvalue >= bestvalue:
                                bestvalue = hvalue
                                besti = i-count+row
                                bestj = j-count+col
                            played = False
                        # print(vmatrix)
                        # raw_input()
        """
        Uncoment this line to see working!
        print(p, bestvalue, besti, bestj)
        """
        return [bestvalue, besti, bestj, moves]

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
