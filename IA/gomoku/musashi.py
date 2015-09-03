# caian 02/09/2015
"""
Artificial Inteligence for the Gomoku game.
"""

from matrix import Matrix
from tree import Tree
from node import Node

class Musashi(object):
    """
    Musashi was a expert samurai who developed the techinique to fight with 2 swords. He was never defeated on combat.
    The main intention to name this as Musashi is the 'double threat' concept to win the game. 2 swords, 'double threat'.
    """
    
    r = Node() # root
    t = Tree() # tree

    def __init__(self, board):
        self.board = board
    
    def domove(self, board):
        """
        The Main method to this AI. Returns a valid move to a given board.
        On my implementation, the board is represented as a 2D Matrix from the import, but could be
        whatever you want.
        """
        self.board = board
        move = self.choose_move() # return a list
        return move

    def choosemove(self):
