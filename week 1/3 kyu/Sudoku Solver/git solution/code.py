def sudoku(puzzle):
    def find_empty_square():
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == 0:
                    return i, j
        return -1, -1

    def is_valid(i, j, num):
        row_valid = all(puzzle[i][x] != num for x in range(9))
        col_valid = all(puzzle[x][j] != num for x in range(9))
        square_valid = all(
            puzzle[i // 3 * 3 + x // 3][j // 3 * 3 + x % 3] != num for x in range(9)
        )
        return row_valid and col_valid and square_valid

    def solve():
        i, j = find_empty_square()
        if i == -1 and j == -1:
            return True
        for num in range(1, 10):
            if is_valid(i, j, num):
                puzzle[i][j] = num
                if solve():
                    return True
                puzzle[i][j] = 0
        return False

    solve()
    return puzzle
