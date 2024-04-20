def validate_board(board: list) -> bool:

    def check_for_dups(field: list) -> bool:
        for line in field:
            line_of_nums = [x for x in line if x.isdigit()]
            if len(line_of_nums) != len(set(line_of_nums)) or "0" in line_of_nums:
                return False
        return True

    if not check_for_dups(board):
        return False

    columns = ["".join([line[i] for line in board]) for i in range(9)]
    if not check_for_dups(columns):
        return False

    board_list = [list(line) for line in board]
    diagonals = []

    for i in range(5):
        diagonal = [board_list[i + j][j] for j in range(5)]
        diagonals.append("".join(diagonal))
    for i in range(1, 5):
        diagonal = [board_list[j][i + j] for j in range(5)]
        diagonals.append("".join(diagonal))

    if not check_for_dups(diagonals):
        return False
    return True
