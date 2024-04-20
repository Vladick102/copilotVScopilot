def snail(snail_map):
    list_of_numbers = []  # Initialize an empty list to store the result

    while snail_map:
        # Traverse the top row (left to right)
        for i in snail_map[0]:
            list_of_numbers.append(i)
        snail_map.pop(0)  # Remove the first row

        if not snail_map:
            break

        # Traverse the last element from each remaining row (top to bottom)
        for j in snail_map:
            list_of_numbers.append(j[-1])
            j.pop()

        # Traverse the last row in reverse (right to left)
        for k in range(len(snail_map[-1]) - 1, -1, -1):
            list_of_numbers.append(snail_map[-1][k])
        snail_map.pop()

        if not snail_map:
            break

        # Traverse the first element from each remaining row in reverse (bottom to top)
        for l in reversed(snail_map):
            list_of_numbers.append(l[0])
            l.pop(0)

    return list_of_numbers
