import numpy as np
from mancala_helpers import *

# A simple evaluation function that simply uses the current score.
def simple_evaluate(state):
    return score_in(state)


def better_evaluate(state):
    return 1.2*score_in(state) 

# depth-limited minimax 
def minimax(state, max_depth, evaluate):
    # returns chosen child state, utility

    # base cases
    if game_over(state): return None, score_in(state)
    if max_depth == 0: return None, evaluate(state)

    # recursive case
    children = [perform_action(action, state) for action in valid_actions(state)]
    results = [minimax(child, max_depth-1, evaluate) for child in children]


    _, utilities = zip(*results)
    player, board = state
    if player == 0: action = np.argmax(utilities)
    if player == 1: action = np.argmin(utilities)
    return children[action], utilities[action]

# runs a competitive game between two AIs:
# better_evaluation (as player 0) vs simple_evaluation (as player 1)
def compete(max_depth, verbose=True):
    state = initial_state()
    while not game_over(state):

        player, board = state
        if verbose: print(string_of(board))
        if verbose: print("--- %s's turn --->" % ["Better","Simple"][player])
        state, _ = minimax(state, max_depth, [better_evaluate, simple_evaluate][player])
    
    score = score_in(state)
    player, board = state
    if verbose:
        print(string_of(board))
        print("Final score: %d" % score)
    
    return score


if __name__ == "__main__":
    
    score = compete(max_depth=4, verbose=True)

