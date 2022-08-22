# Solve sudoku using backtracking method
def next_empty_spot(puzzle):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                return row, col

    return None, None

def is_valid(puzzle, guess, row, col):
    
    if guess in puzzle[row]:
        return False

    col_check = [puzzle[r][col] for r in range(9)]
    if guess in col_check:
        return False

    row_index = row // 3
    col_index = col // 3

    for r in range(row_index * 3, (row_index + 1) * 3):
        for c in range(col_index * 3, (col_index + 1) * 3):
            if puzzle[r][c] == guess:
                return False

    return True

def print_puzzle(puzzle):
    for row in puzzle:
        print(row)

def solve_sudoku(puzzle):
    next_row, next_col = next_empty_spot(puzzle)

    if next_row is None: # No more empty spots to fill
        return True

    for guess in range(1, 10):
        if is_valid(puzzle, guess, next_row, next_col):
            puzzle[next_row][next_col] = guess

            if solve_sudoku(puzzle):
                return True

        puzzle[next_row][next_col] = 0

    return False

if __name__ == '__main__':
    puzzle = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 7, 3, 0, 0],
        [7, 4, 0, 0, 0, 3, 5, 6, 0],
        [0, 1, 3, 0, 7, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 9],
        [0, 0, 9, 0, 0, 2, 0, 0, 4],
        [0, 0, 0, 3, 0, 5, 9, 0, 0],
        [9, 0, 0, 0, 0, 6, 0, 0, 1],
        [6, 0, 5, 0, 0, 0, 0, 0, 0]
    ]

    solve_sudoku(puzzle)
    print_puzzle(puzzle)