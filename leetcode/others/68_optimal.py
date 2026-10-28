# Solve sudoku

# backtracking with constraint tracking.


def solve_sudoku(board):

    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    empty = []

    # Initialize sets and collect empty cells
    for row in range(9):
        for col in range(9):

            num = board[row][col]

            if num == ".":
                empty.append((row, col))
            else:
                box = (row // 3) * 3 + col // 3

                rows[row].add(num)
                cols[col].add(num)
                boxes[box].add(num)

    return backtrack(board, empty, 0, rows, cols, boxes)


def backtrack(board, empty, index, rows, cols, boxes):

    if index == len(empty):
        return True

    row, col = empty[index]
    box = (row // 3) * 3 + col // 3

    for num in "123456789":

        # Check constraints in O(1)
        if (num in rows[row] or
            num in cols[col] or
            num in boxes[box]):
            continue

        # Place number
        board[row][col] = num
        rows[row].add(num)
        cols[col].add(num)
        boxes[box].add(num)

        if backtrack(board, empty, index + 1,
                     rows, cols, boxes):
            return True

        # Backtrack
        board[row][col] = "."
        rows[row].remove(num)
        cols[col].remove(num)
        boxes[box].remove(num)

    return False


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
