n = int(input("Enter the number of queens: "))
print('\n')
def printSolution(board):
    for i in range(n):
        for j in range(n):
            print (board[i][j],end='   ')
        print('\n')
def isSafe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True
def solveNQUtil(board, col):
    if col >= n:
        return True
    for i in range(n):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveNQUtil(board, col + 1):
                return True
            board[i][col] = 0
    return False

def solveNQ():
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solveNQUtil(board, 0):
        print("Solution does not exist")
    printSolution(board)
solveNQ()
