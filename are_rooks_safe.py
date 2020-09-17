# simulates a chess board with a number of rooks and determines if any of them can capture each other
# this is a 2d array problem

# chessboard can be any size from 1x1 to 99x99
# if rooks are safe -> True, otherwise, -> False
# test case 4x4 array with 3 rooks on the board

board = [
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,0],
    [0,0,0,1]
]

board1 = [
    [0,0,1,0],
    [0,0,1,0],
    [0,1,0,0],
    [0,0,0,1]
]

board2 = [
    [0,0,1,0],
    [1,0,0,0],
    [0,1,0,0],
    [0,0,0,1]
]

board3 = [
    [0,1],
    [1,0]
]

board4 = [[1]]

def rooks_safe(board):
    n = len(board)
    
    for row_i in range(n):
        row_count = 0
        for col_i in range(n):
            row_count += board[row_i][col_i]
        if row_count > 1:
            print('False')
            return False
        
    for col_i in range(n):
        col_count = 0
        for row_i in range(n):
            col_count += board[row_i][col_i]
        if col_count > 1:
            print('False')
            return False
    
    print('True - Rooks are Safe!')
    return True
            

rooks_safe(board)
rooks_safe(board1)
rooks_safe(board2)
rooks_safe(board3)
rooks_safe(board4)

