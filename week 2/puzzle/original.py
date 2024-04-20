def validate_board(board: list) -> bool:

    def check_for_dups(field: list) -> bool:
        for line in field:
            line_of_nums = line.strip("*")
            line_of_nums = line_of_nums.replace(" ", "")
            if any(line_of_nums.count(x) > 1 for x in line_of_nums):
                return False
            if "0" in line_of_nums:
                return False
        return True

    if not check_for_dups(board):
        return False

    column = []
    list_of_columns = []
    for num_column in range(9):
        for line in board:
            column += [line[num_column]]
        list_of_columns += ["".join(column)]
        column = []

    if not check_for_dups(list_of_columns):
        return False

    board_list = []
    for line in board:
        board_list += [list(line)]

    angle = []
    colors = []
    line = 4
    for col in range(4, -1, -1):
        for row in range(5):
            angle += board_list[line - row][col]
        for column in range(1, 5):
            angle += board_list[line][col + column]
        colors += ["".join(angle)]
        angle = []
        line += 1

    if not check_for_dups(colors):
        return False
    return True
