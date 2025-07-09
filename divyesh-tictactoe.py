import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board): # passes tests
    """
    Returns player who has the next turn on a board.
    """
    has_empty = any(EMPTY in sublist for sublist in board)
    if not has_empty:
        return X
    
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    if (x_count > o_count):
        return O
    else:
        return X
    
    raise NotImplementedError


def actions(board): # passes tests
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    if board[0][0] is None:
        actions_set.add((0, 0))
    if board[0][1] is None:
        actions_set.add((0, 1))
    if board[0][2] is None:
        actions_set.add((0, 2))
    if board[1][0] is None:
        actions_set.add((1, 0))
    if board[1][1] is None:
        actions_set.add((1, 1))
    if board[1][2] is None:
        actions_set.add((1, 2))
    if board[2][0] is None:
        actions_set.add((2, 0))
    if board[2][1] is None:
        actions_set.add((2, 1))
    if board[2][2] is None:
        actions_set.add((2, 2))

    return actions_set
    raise NotImplementedError


def result(board, action): # passes tests
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    if new_board[action[0]][action[1]] is not None:
        raise ValueError("Invalid action: Cell already occupied.")
    
    if action[0] < 0 or action[0] > 2 or action[1] < 0 or action[1] > 2:
        raise ValueError("Invalid action: Indices out of bounds.")
    
    new_board[action[0]][action[1]] = player(board)
    return new_board
    raise NotImplementedError


def winner(board): # passes tests
    """
    Returns the winner of the game, if there is one.
    """
    diagnal1 = [board[i][i] for i in range(3)]
    diagnal2 = [board[i][2 - i] for i in range(3)]
    if all(cell == X for cell in diagnal1) or all(cell == X for cell in diagnal2):
        return X
    if all(cell == O for cell in diagnal1) or all(cell == O for cell in diagnal2):
        return O
    
    for row in board:
        if all(cell == X for cell in row):
            return X
        if all(cell == O for cell in row):
            return O
        
    for col in range(3):
        if all(board[row][col] == X for row in range(3)):
            return X
        if all(board[row][col] == O for row in range(3)):
            return O
    return None  # No winner yet
    raise NotImplementedError


def terminal(board): # passes tests
    """
    Returns True if game is over, False otherwise.
    """
    result_winner = winner(board)
    if result_winner is not None:
        return True # Game is over with a winner
    
    has_empty = any(EMPTY in sublist for sublist in board)
    if not has_empty:
        return True # Game is over with a draw (no empty cells)
    
    return False  # Game is still ongoing
    raise NotImplementedError


def utility(board): # passes tests
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result_winner = winner(board)
    if result_winner == X:
        return 1
    elif result_winner == O:
        return -1
    else:
        return 0
    raise NotImplementedError


#############################################################


# Python3 program to find the next optimal move for a player
   
# This is the minimax_core function. It considers all 
# the possible ways the game can go and returns the value of the board 
def minimax_core(board, depth, isMax): 
    the_winner = winner(board)
    score = None
    if the_winner is X:
        score = 1
    elif the_winner is O:
        score = -1
    else:
        score = 0

    # If Maximizer has won the game return his/her evaluated score 
    if (score == 1) : 
        return score

    # If Minimizer has won the game return his/her evaluated score 
    if (score == -1) :
        return score

    # If there are no more moves and no winner then it is a tie 
    if (terminal(board) == True) :
        return 0

    # If this maximizer's move 
    if (isMax) :     
        best = -1000 

        # Traverse all cells 
        for i in range(3) :         
            for j in range(3) :
                # Check if cell is empty 
                if (board[i][j]== EMPTY) :
                    # Make the move 
                    board[i][j] = X 

                    # Call minimax recursively and choose the maximum value 
                    best = max(best, minimax_core(board, depth + 1, not isMax) )

                    # Undo the move 
                    board[i][j] = EMPTY
        return best

    # If this minimizer's move 
    else :
        best = 1000 

        # Traverse all cells 
        for action in actions(board):         
            new_board = result(board, action)

            # Call minimax recursively and choose the minimum value 
            best = min(best, minimax_core(new_board, depth + 1, not isMax))

        return best

# This will return the best possible move for the player 
def minimax(board) : 
    bestVal = -1000 
    bestMove = (-1, -1) 

    # Traverse all cells, evaluate minimax function for 
    # all empty cells. And return the cell with optimal value. 
    for i in range(3) :     
        for j in range(3) :
            # Check if cell is empty 
            if (board[i][j] == EMPTY) : 
                # Make the move 
                board[i][j] = X

                # compute evaluation function for this move. 
                moveVal = minimax_core(board, 0, False) 

                # Undo the move 
                board[i][j] = EMPTY

                # If the value of the current move is 
                # more than the best value, then update best
                if (moveVal > bestVal) :                
                    bestMove = (i, j)
                    bestVal = moveVal

    print("The value of the best Move is :", bestVal)
    print()
    return bestMove

# Driver code
board = [
    [ X, O, X ], 
    [ O, O, X ], 
    [ EMPTY, EMPTY, EMPTY ] 
]

bestMove = minimax(board)

print("The Optimal Move is :") 
print("ROW:", bestMove[0], " COL:", bestMove[1])

# This code is contributed by divyesh072019