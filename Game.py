class State:

    def __init__(self, visited=None):
        pass


def GetActions(CurrentState):
    """
    Input:
        CurrentState: The state of the game at the current moment

    Returns:
        List of all legal actions from the current state

    """
    pass


def ApplyAction(CurrentState, Action):
    """
    Input:
        CurrentState: The state of the game at the current moment
        Action: A legal action to be performed

    Returns:
        The next state that results from applying the action

    """
    pass


def GetNextStates(CurrentState):
    """
    Input:
        CurrentState: The state of the game at the current moment

    Returns:
        A list of all states that result from applying all possible transitions at the current state

    """
    pass


def IsTerminal(CurrentState):
    """
    Input:
        CurrentState: The state of the game at the current moment

    Returns:
        True if the current state is terminal, false otherwise

    """
    pass


def GetStateRepresentation(CurrentState):
    """
    Input:
        CurrentState: The state of the game at the current moment

    Returns:
        A string representation of the state

    """
    pass


def GetResult(CurrentState):
    """
    Input:
        CurrentState: The state of the game at the current moment

    Returns:
        True if the state is terminal and the game was won, false otherwise

    """
    pass

