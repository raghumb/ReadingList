# Validate a 9×9 Sudoku Board

"""
    A board is valid if:
1. Each row contains no repeated digits from 1 to 9.
2. Each column contains no repeated digits from 1 to 9.
3. Each 3×3 sub-box contains no repeated digits from 1 to 9.

. represents an empty cell and should be ignored. The board does not need to be completely filled to be valid.
    """
    
    
# o(1)
def is_valid_sudoku(board):

    # Step 1: Check rows
    for row in range(9):
        arr = []

        for col in range(9):
            if board[row][col] != '.':
                arr.append(board[row][col])

        if len(arr) != len(set(arr)):
            return False

    # Step 2: Check columns
    for col in range(9):
        arr = []

        for row in range(9):
            if board[row][col] != '.':
                arr.append(board[row][col])

        if len(arr) != len(set(arr)):
            return False

    # Step 3: Check 3x3 boxes
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            arr = []

            for row in range(box_row, box_row + 3):
                for col in range(box_col, box_col + 3):
                    if board[row][col] != '.':
                        arr.append(board[row][col])

            if len(arr) != len(set(arr)):
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

print(is_valid_sudoku(board))



###### WITH LIST COMP#####

def is_valid_sudoku(board):

    # Step 1: Check rows
    for row in range(9):
        arr = [board[row][col] for col in range(9)
               if board[row][col] != '.']

        if len(arr) != len(set(arr)):
            return False

    # Step 2: Check columns
    for col in range(9):
        arr = [board[row][col] for row in range(9)
               if board[row][col] != '.']

        if len(arr) != len(set(arr)):
            return False

    # Step 3: Check 3x3 boxes
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):

            arr = [
                board[row][col]
                for row in range(box_row, box_row + 3)
                for col in range(box_col, box_col + 3)
                if board[row][col] != '.'
            ]

            if len(arr) != len(set(arr)):
                return False

    return True


print(is_valid_sudoku(board))