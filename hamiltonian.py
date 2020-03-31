import numpy as np
import itertools as iter
import copy
import random

'''
Hamiltonian cycle problem single game implementation

'''


class State:
    def __init__(self,  visited, last_visited=None, first_visited=None, game_params=None):

        self.last_visited=last_visited
        self.visited = visited
        self.first_visited = first_visited

        # start graph if this is the first state (game parameters)
        if not game_params:
            # randomize graph and set game params
            n = 4
            adjacency = [[random.randint(0, 1) for _ in range(n)] for _ in range(n)]

            # game_params = (set of all nodes, adjacency matrix, first node of the cycle)
            self.game_params = (set([i for i in range(n)]), adjacency)
        else:
            self.game_params=game_params


def GetActions(CurrentState):

    # get graph configuration via state's game parameters
    next_nodes = []
    available_nodes = CurrentState.game_params[0].difference(CurrentState.visited)
    adjacency = CurrentState.game_params[1]
    #for base case, initialized with root as last visited 

    # if this is the first pick the last_visited is none
    if CurrentState.last_visited is None:
        return list(available_nodes)

    # see if current node has any path to other available nodes
    for node in available_nodes:
        if adjacency[CurrentState.last_visited][node]:
            next_nodes.append(node)

    return next_nodes

def ApplyAction(CurrentState, Action):
    # visit next node and add to visited
    #when do add root vertex
    new_set=set()
    new_set.add(Action)
    new_visited = CurrentState.visited.union(new_set)

    # check if this is the first node to visit
    # if this is the case, add the action as the first node visited from the cycle
    if CurrentState.first_visited is None:
        CurrentState.first_visited = Action

    State2 = State(
        new_visited,
        Action,
        CurrentState.first_visited,
        CurrentState.game_params
    )
    return State2

def GetNextStates(CurrentState):

    # get next states
    Actions = GetActions(CurrentState)

    # if dead end is reached return None??? I don't know what to do here
    if not Actions:
        return None
    
    next_states=[]
    for i in Actions:
        new =ApplyAction(CurrentState, i)
        next_states.append(new)
    return next_states

def IsTerminal(CurrentState):

    # all nodes have been visited
    if len(CurrentState.visited) == len(CurrentState.game_params[0]):
        return True

    # try to get a next state, if none exists then dead end so it is terminal
    next_state = GetNextStates(CurrentState)

    if not next_state:
        return True
    else:
        return False

def GetStateRepresentation(CurrentState):
    return (CurrentState.last_visited, CurrentState.visited, CurrentState.game_params[1])


def GetResult(CurrentState):

    # TODO: Not sure if this is the right approach
    # score is 1 if reached a hamiltonian cycle, else it is always zero
    if IsTerminal(CurrentState) and len(CurrentState.visited) == len(CurrentState.game_params[0]):

        # check if we can connect the last visited node to the first visited node of the
        # cycle after going through all nodes
        adjacency = CurrentState.game_params[1]
        first_visited = CurrentState.first_visited
        if CurrentState.last_visited==CurrentState.first_visited:
            return 1
        else:
            return 0
    else:
        return 0
