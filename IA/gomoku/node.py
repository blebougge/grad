# caian 03/09/2015
"""
Node class for the Tree.
"""

def Node(object):
    """
    Node for the Tree in the Gomoku game.
    Variable 'data' could be whatever you want. Children must be a list of Nodes.

        self.data = <your data>
        self.children = [child1, child2, ...]

    """

    def __init__(self, data=None, children=None):
        self.data = data
        self.children = children

    def child(self, position):
        """
        Returns the child in the position.
        """
        if self.children[position] != None:
            return self.children[position]
        return None

    def addchild(self, child):
        """
        Add a child to children nodes.
        """
        self.children.append(child)

    def rmchild(self, child):
        """
        Remove a specific child from children nodes.
        """
        self.children.remove(child)
