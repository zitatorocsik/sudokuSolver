import numpy as np
import math

f = open("sudoku.txt", "r")

size = int(f.readline().strip())
board = list()

for n in range(size):
    row = [int(x) for x in f.readline().strip()]
    board.append(row)


def canPlace(row, col, n):
    # check row for n
    for c in range(size):
        if board[row][c] == n:
            return False
    
    # check column for n
    for r in range(size):
        if board[r][col] == n:
            return False

    # check own grid only if size is a square number
    grid = int(math.sqrt(size))
    if grid * grid == size:
        # row - row mod math.sqrt(size)
        for r in range(row-(row % grid), (row-(row % grid))+grid):
            for c in range(col-(col % grid), (col-(col % grid))+grid):
                if board[r][c] == n:
                    return False
    return True


def solve():
    global board
    for row in range(size):
        for col in range(size):
            if board[row][col] == 0:
                for n in range(1, size+1):
                    if canPlace(row, col, n):
                        board[row][col] = n
                        solve()
                        board[row][col] = 0
                return
    print(np.matrix(board))


print("Welcome to SudokuSolve")
print("Here is your board:")
print(np.matrix(board))
print("Solution:")
solve()




