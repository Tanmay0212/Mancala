
from os import stat


def pad(num: int) -> str:
    return str(num).rjust(2,"0") 


def pad_all(nums: list) -> list:
    new_nums = []
    for n in nums:
        new_nums.append(pad(n))

    return new_nums 


def initial_state() -> tuple:
    board = [4,4,4,4,4,4,4,0,4,4,4,4,4,4,4,0]
    player = 0
    return (player, board) 


def game_over(state: tuple) -> bool:
   
    for x in range (0,7):
        if(state[1][x] != 0):
            return False
    
    for x in range (9,14):
        if(state[1][x] != 0):
            return False
    
    return True 

def valid_actions(state: tuple) -> list:

    action0 = []
    action1 = []

    if(state[0] == 0):
        for x in range(0,7):
            if(state[1][x]!=0):
                action0.append(x)
        return action0

    if(state[0] == 1):
        for x in range(8,15):
            if(state[1][x]!=0):
                action1.append(x)
        return action1



def mancala_of(player: int) -> int:
    if(player==0):
        return 7
    else:
        return 15
    


def pits_of(player: int) -> list:

    if(player==0):
        return(list(range(0,7)))

    if(player==1):
        return(list(range(8,15)))

    


def player_who_can_do(move: int) -> int:

    if 0 <= move <= 6:
        return 0
    if 8 <= move <= 14:
        return 1
   
    


def opposite_from(position: int) -> int:


    return abs(14-position) 


def play_turn(move: int, board: list) -> tuple:

    new_board = list(board)

    no_gems = new_board[move]

    player = player_who_can_do(move)

    new_board[move] = 0

    move += 1
    while(no_gems!=1):
        if(move == mancala_of(1-player)):
            move += 1
            continue
        else:
            no_gems -= 1
            new_board[move % 16] += 1
            move += 1
    
    if(new_board[move % 16] ==0 and new_board[opposite_from(move % 16)] != 0 and move in pits_of(player)):
        new_board[mancala_of(player)] += new_board[move % 16] + no_gems + new_board[opposite_from(move % 16)]
        new_board[opposite_from(move % 16)] = 0
    elif(move == mancala_of(1-player)):
        move += 1
        new_board[move % 16] += 1
    else:
        new_board[move % 16] += 1


    if(move == mancala_of(player)):
        return (player, new_board)

    return (1-player, new_board)


            
def clear_pits(board: list) -> list:
    new_board = board
    if (valid_actions((0,new_board))) == []:
        for pit in pits_of(1):
            new_board[mancala_of(1)] += new_board[pit]
            new_board[pit] = 0
    else:
        for pit in pits_of(0):
            new_board[mancala_of(0)] += new_board[pit]
            new_board[pit] = 0


    
    return new_board 


def perform_action(action, state):
    player, board = state
    new_player, new_board = play_turn(action, board)
    if 0 in [len(valid_actions((0, new_board))), len(valid_actions((1, new_board)))]:
        new_board = clear_pits(new_board)
    return new_player, new_board


def score_in(state: tuple) -> int:
    return (state[1][7]-state[1][15]) 


def is_tied(board: list) -> bool:
    if(board[7]-board[15] == 0):
        return True
    else:
        return False


def winner_of(board: list) -> int:
    if(board[7] > board[15]):
        return 0
    else:
        return 1


def string_of(board: list) -> str:
    opp_pits = " "*10
    mancala = " "*8
    play_pit = " "*10

    rev = reversed(board[8:15])
    opp_pits1 = pad_all(rev)

    for i in opp_pits1:

        opp_pits += " "+i

    mancala += pad((board[15])) + "                      " + pad(board[7])
    play_pit1 = pad_all(board[0:7])
    for i in play_pit1:

        play_pit += " "+i

    return "\n" + opp_pits + "\n" + mancala + "\n" + play_pit + "\n" 

