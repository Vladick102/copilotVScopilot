from itertools import permutations as it_permutations


def permutations(input_string):
    return sorted(
        "".join(p) for p in set(it_permutations(input_string, len(input_string)))
    )
