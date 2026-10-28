# Solve sudoku


def is_valid(board, row, col, num):

    # Check row
    for j in range(9):
        if board[row][j] == num:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


def solve_sudoku(board):

    for row in range(9):
        for col in range(9):

            if board[row][col] == ".":

                for num in "123456789":

                    if is_valid(board, row, col, num):

                        board[row][col] = num

                        if solve_sudoku(board):
                            return True

                        # Backtrack
                        board[row][col] = "."

                return False

    return True


board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

if solve_sudoku(board):
    for row in board:
        print(" ".join(row))
else:
    print("No solution")
