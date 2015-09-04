# caian 03/09/2015
"""
Tree for the Artificial Inteligence
"""

from node import Node

class Tree(object):
    """
    To implement all the possibe moves in the Gomoku Game, a Tree is required.
    That is the Tree I've implemented.

    The root node is the actual state of the board.
    """
    
    def __init__(self, root=None):
        self.root = root
    
    def addchild(self, node):
        """
        Add nodes to the specific depth.
        """
        self.root.addchild(node)

    def rmchild(self, child):
        """
        Remove a specific child from children nodes.
        """
        self.root.rmchild(child)
