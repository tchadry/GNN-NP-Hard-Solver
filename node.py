
'''
Node class implementation for MCTS. Really simple, can add more functionalities
later
'''
class Node:

    def __init__(self, state):

        #place the state of the game represented in this node
        self.state=state

        #initialize children and parents, and wins
        self.wins=0
        self.parent=None
        self.children = []
        self.visits=0
        self.weight=0
        self.sputc = 0.0
        self.ressq = 0.0

    def add_child(self, child):

        #we have to update the children of this node and add itself as
        #the parent of the child
        self.children.append(child)
        child.parent = self


