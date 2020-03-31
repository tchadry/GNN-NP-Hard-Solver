import node as nd
import numpy as np
import MCTS as mcts
import hamiltonian as game
import random

'''

The starting node will be randomized since for a hamiltonian cycle, independent of the node you start, if there is a solution
you should be able to find one.

For this problem, we will only test inputs which we know there a Hamiltonian cycle exist
'''




visited=set()
n=8
first  = random.randint(0,n-1)
print("Initial node is: ", first)

#our game parameters
#first test case: octagon directed cycle with first node connected to the second, which is connected to the third, and so on until the cycle
#Expected output: depends on the first node but assuming for example first node was 0  - [1,2,3,4,5,6,7,0]
adjacency1=[[0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0]]
game_params1=(set([i for i in range(n)]), adjacency1)

#second test case: octagon directed cycle with some of the edges crossed 
#Expected output: depends on the first node but assuming for example first node was 0  - [1,2,3,5,4,7,6,0]
adjacency2=[[0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,0],[1,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0]]
game_params2=(set([i for i in range(n)]), adjacency2)


print("First test case:")
#initializing tree 
RootState = game.State(visited,first,first, game_params=game_params1)
Root = nd.Node(RootState)
print("Nodes created")

x = mcts.MCTS(Root,game)
print("MCTS created")

x.Run()

print("Iterations finished")

#we are going to start from the root node in the resulting MCTS tree, and do a DFS to pick the maximum value node at each level, until we
#get to a leaf node (terminal state). The resulting path will be the optimal result from the MCTS
result=[]
child=False
if len(Root.children)>0:
    child=True
while (child):
    max=0
    childrenn = Root.children
    for i in childrenn:
        if i.sputc>max:
            max=i.sputc
            Root = i
    result.append(game.GetStateRepresentation(Root.state)[0])
    if (len(Root.children)==0):
        child=False

print(result)

print("Second test case")
#initializing tree 
RootState = game.State(visited,first,first, game_params=game_params2)
Root = nd.Node(RootState)
print("Nodes created")

x = mcts.MCTS(Root,game)
print("MCTS created")

x.Run()

print("Iterations finished")

#we are going to start from the root node in the resulting MCTS tree, and do a DFS to pick the maximum value node at each level, until we
#get to a leaf node (terminal state). The resulting path will be the optimal result from the MCTS
result=[]
child=False
if len(Root.children)>0:
    child=True
while (child):
    max=0
    childrenn = Root.children
    for i in childrenn:
        if i.sputc>max:
            max=i.sputc
            Root = i
    result.append(game.GetStateRepresentation(Root.state)[0])
    if (len(Root.children)==0):
        child=False

print(result)



