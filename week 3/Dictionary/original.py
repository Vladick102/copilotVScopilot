"""
Make a dictionary with spelling.
"""
def dict_reader_tuple(file_dict: str) -> list:
    """
    Function reads a file and makes list of tuples.
    values are their spelling.
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmpfile:
    ...     _ = tmpfile.write('NACHOS 2 N AE1 CH OW0 Z')
    >>> dict_reader_tuple(tmpfile.name)
    [('NACHOS', 2, ['N', 'AE1', 'CH', 'OW0', 'Z'])]
    """
    tuple_list = []
    with open(file_dict, 'r', encoding='UTF-8') as file:
        lines = file.readlines()
        for line in lines:
            slices = line.strip().split()
            word = slices[0]
            number = int(slices[1])
            sound = slices[2:]
            tuple_list.append((word, number, sound))
    return tuple_list
def dict_reader_dict(file_dict):
    """
    Function reads a file and makes a dictionary, where keys are words and
    values are their spelling.
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmpfile:
    ...     _ = tmpfile.write('NACHOS 2 N AE1 CH OW0 Z\\nNACHOS 1 N AA1 CH OW0 Z')
    >>> dict_reader_dict(tmpfile.name)
    {'NACHOS': {('N', 'AE1', 'CH', 'OW0', 'Z'), ('N', 'AA1', 'CH', 'OW0', 'Z')}}
    """
    with open(file_dict, 'r', encoding='UTF-8') as file:
        lines = file.readlines()
        word_dict = {}
        for line in lines:
            slices = line.strip().split()
            word = slices[0]
            sounds = tuple(slices[2:])
            if word in word_dict:
                word_dict[word].add(sounds)
            else:
                word_dict[word] = {sounds}
    return word_dict
def dict_invert(dct: dict) -> dict:
    """
    Function reads a file and makes a dictionary, where keys are words and
    values are their spelling.
    >>> dict_invert({'WATER':{('W','A','T','E','R')}})
    {1: {('WATER', ('W', 'A', 'T', 'E', 'R'))}}
    """
    if isinstance(dct, list):
        dct_list = {}
        for i in dct:
            key = i[0]
            val = tuple(i[2])
            if key in dct_list:
                dct_list[key].add(val)
            else:
                dct_list[key] = {val}
        return dct_list
    if isinstance(dct, dict):
        result = {}
        for key, val in dct.items():
            len_val = len(val)
            if len_val in result:
                result[len_val].add((key, *val))
            else:
                result[len_val] = {(key, *val)}
        sorted_d = {k: v for k, v in sorted(result.items())}
        return sorted_d
if __name__ == "__main__":
    import doctest
    print(doctest.testmod())