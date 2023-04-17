from pyteal import *

# Define the PyTeal program

board = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
turn = 0
while board[0] == 0:
    if (turn % 2) == 0:
        player_move = input()
        if board[int(player_move)] == 0:
            board[int(player_move)] = 1
        else:
            board[0] = 2
    elif turn == 1:
        if board[5] == 1:
            board[7] = 2
    elif turn == 3:
        if board[5] == 1:
            if board[1] == 1:
                board[9] = 2
            elif board[2] == 1:
                board[8] = 2
            elif board[3] == 1:
                board[1] = 2
            elif board[4] == 1:
                board[6] = 2
            elif board[6] == 1:
                board[4] = 2
            elif board[8] == 1:
                board[2] = 2
            elif board[9] == 1:
                board[1] = 2
    elif turn == 5:
        if board[5] == 1 and board[1] == 1:
            if board[8] == 1:
                board[2] = 2
            else:
                board[8] = 2
                board[0] = 2 #comp wins
        if board[5] == 1 and board[2] == 1:
            if board[9] == 1:
                board[1] = 2
            else:
                board[9] = 2
                board[0] = 2 #comp wins
        if board[5] == 1 and board[3] == 1:
            if board[4] == 1:
                board[6] = 2
            else:
                board[4] = 2
                board[0] = 2 #comp wins
    turn += 1
    if (turn % 2) == 0:
        print("turn:", turn, "status:", board[0])
        print (board[1], board[2], board[3])
        print (board[4], board[5], board[6])
        print (board[7], board[8], board[9])

        
program = Return(Int(board[0]))

# Compile the program to Teal bytecode
compiled_program = compileTeal(program, Mode.Application)

# Print the compiled program
print(compiled_program)