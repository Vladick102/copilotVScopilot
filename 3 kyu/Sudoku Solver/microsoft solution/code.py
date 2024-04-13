def sudoku(puzzle):
    # Create a copy of the puzzle to avoid modifying the original
    puzzle_copy = [row[:] for row in puzzle]

    def is_valid(puzzle, row, col, num):
        for x in range(9):
            if puzzle[row][x] == num:
                return False
        for x in range(9):
            if puzzle[x][col] == num:
                return False
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if puzzle[i + start_row][j + start_col] == num:
                    return False
        return True

    def solve(puzzle):
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == 0:
                    for num in range(1, 10):
                        if is_valid(puzzle, i, j, num):
                            puzzle[i][j] = num
                            if solve(puzzle):
                                return True
                            puzzle[i][j] = 0
                    return False
        return True

    if solve(puzzle_copy):
        return puzzle_copy
    else:
        return "No solution exists"
