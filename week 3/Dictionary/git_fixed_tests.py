import unittest
import tempfile
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
            if len(slices) >= 3:
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
    {'NACHOS': {('N', 'AE1', 'CH', 'OW0', 'Z'), ('N', 'AA1', 'CH', 'OW0', 'Z')}
     """
    with open(file_dict, 'r', encoding='UTF-8') as file:
        lines = file.readlines()
        word_dict = {}
        for line in lines:
            slices = line.strip().split()
            if len(slices) >= 3:
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
        result = {}
        for item in dct:
            key = item[0]
            val = tuple(item[2])
            if key in result:
                result[key].add(val)
            else:
                result[key] = {val}
        dct = result
    if isinstance(dct, dict):
        result = {}
        for key, val_set in dct.items():
            len_val = len(val_set)
            for val in val_set:
                if len_val in result:
                    result[len_val].add((key, val))
                else:
                    result[len_val] = {(key, val)}
        return {k:result[k] for k in sorted(result)}
input_list = [
            ('ZUCCARELLI', 1, ['Z', 'UW0', 'K', 'ER0', 'EH1', 'L', 'IY0']),
            ('ZUCCARO', 1, ['Z', 'UW0', 'K', 'AA1', 'R', 'OW0']),
            ('ZUCCHINI', 1, ['Z', 'UW0', 'K', 'IY1', 'N', 'IY0']),
            ('ZUCCO', 1, ['Z', 'UW1', 'K', 'OW0']),
            ('ZUCH', 1, ['Z', 'AH1', 'CH']),
            ('ZUCHOWSKI', 1, ['Z', 'AH0', 'HH', 'AO1', 'F', 'S', 'K', 'IY0']),
            ('ZUCHOWSKI', 2, ['Z', 'UW0', 'K', 'AO1', 'F', 'S', 'K', 'IY0']),
            ('ZUCK', 1, ['Z', 'AH1', 'K']),
            ('ZUCKER', 1, ['Z', 'AH1', 'K', 'ER0']),
            ('ZUCKER', 2, ['Z', 'UW1', 'K', 'ER0']),
            ('ZUCKERMAN', 1, ['Z', 'AH1', 'K', 'ER0', 'M', 'AH0', 'N']),
            ('ZUCKERMAN', 2, ['Z', 'UW1', 'K', 'ER0', 'M', 'AH0', 'N']),
            ('ZUCKERMAN\'S', 1, ['Z', 'AH1', 'K', 'ER0', 'M', 'AH0', 'N', 'Z']),
            ('ZUCKERMAN\'S', 2, ['Z', 'UW1', 'K', 'ER0', 'M', 'AH0', 'N', 'Z']),
            ('ZUCKER\'S', 1, ['Z', 'AH1', 'K', 'ER0', 'Z'])
        ]
class TestDictFunctions(unittest.TestCase):
    def test_dict_reader_tuple(self):
        input_lines = [
            'ZUCCARELLI 1 Z UW0 K ER0 EH1 L IY0',
            'ZUCCARO 1 Z UW0 K AA1 R OW0',
            'ZUCCHINI 1 Z UW0 K IY1 N IY0',
            'ZUCCO 1 Z UW1 K OW0',
            'ZUCH 1 Z AH1 CH',
            'ZUCHOWSKI 1 Z AH0 HH AO1 F S K IY0',
            'ZUCHOWSKI 2 Z UW0 K AO1 F S K IY0',
            'ZUCK 1 Z AH1 K',
            'ZUCKER 1 Z AH1 K ER0',
            'ZUCKER 2 Z UW1 K ER0',
            'ZUCKERMAN 1 Z AH1 K ER0 M AH0 N',
            'ZUCKERMAN 2 Z UW1 K ER0 M AH0 N',
            'ZUCKERMAN\'S 1 Z AH1 K ER0 M AH0 N Z',
            'ZUCKERMAN\'S 2 Z UW1 K ER0 M AH0 N Z',
            'ZUCKER\'S 1 Z AH1 K ER0 Z'
        ]
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp:
            temp.write('\n'.join(input_lines))
            temp.seek(0)
            result = dict_reader_tuple(temp.name)
        expected = [
            ('ZUCCARELLI', 1, ['Z', 'UW0', 'K', 'ER0', 'EH1', 'L', 'IY0']),
            ('ZUCCARO', 1, ['Z', 'UW0', 'K', 'AA1', 'R', 'OW0']),
            ('ZUCCHINI', 1, ['Z', 'UW0', 'K', 'IY1', 'N', 'IY0']),
            ('ZUCCO', 1, ['Z', 'UW1', 'K', 'OW0']),
            ('ZUCH', 1, ['Z', 'AH1', 'CH']),
            ('ZUCHOWSKI', 1, ['Z', 'AH0', 'HH', 'AO1', 'F', 'S', 'K', 'IY0']),
            ('ZUCHOWSKI', 2, ['Z', 'UW0', 'K', 'AO1', 'F', 'S', 'K', 'IY0']),
            ('ZUCK', 1, ['Z', 'AH1', 'K']),
            ('ZUCKER', 1, ['Z', 'AH1', 'K', 'ER0']),
            ('ZUCKER', 2, ['Z', 'UW1', 'K', 'ER0']),
            ('ZUCKERMAN', 1, ['Z', 'AH1', 'K', 'ER0', 'M', 'AH0', 'N']),
            ('ZUCKERMAN', 2, ['Z', 'UW1', 'K', 'ER0', 'M', 'AH0', 'N']),
            ('ZUCKERMAN\'S', 1, ['Z', 'AH1', 'K', 'ER0', 'M', 'AH0', 'N', 'Z']),
            ('ZUCKERMAN\'S', 2, ['Z', 'UW1', 'K', 'ER0', 'M', 'AH0', 'N', 'Z']),
            ('ZUCKER\'S', 1, ['Z', 'AH1', 'K', 'ER0', 'Z'])
        ]
        self.assertEqual(result, expected)

    def test_dict_reader_dict(self):
        input_lines = [
            'ZUCCARELLI 1 Z UW0 K ER0 EH1 L IY0',
            'ZUCCARO 1 Z UW0 K AA1 R OW0',
            'ZUCCHINI 1 Z UW0 K IY1 N IY0',
            'ZUCCO 1 Z UW1 K OW0',
            'ZUCH 1 Z AH1 CH',
            'ZUCHOWSKI 1 Z AH0 HH AO1 F S K IY0',
            'ZUCHOWSKI 2 Z UW0 K AO1 F S K IY0',
            'ZUCK 1 Z AH1 K',
            'ZUCKER 1 Z AH1 K ER0',
            'ZUCKER 2 Z UW1 K ER0',
            'ZUCKERMAN 1 Z AH1 K ER0 M AH0 N',
            'ZUCKERMAN 2 Z UW1 K ER0 M AH0 N',
            'ZUCKERMAN\'S 1 Z AH1 K ER0 M AH0 N Z',
            'ZUCKERMAN\'S 2 Z UW1 K ER0 M AH0 N Z',
            'ZUCKER\'S 1 Z AH1 K ER0 Z'
        ]
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp:
            temp.write('\n'.join(input_lines))
            temp.seek(0)
            result = dict_reader_dict(temp.name)
        expected = {'ZUCCARELLI': {('Z', 'UW0', 'K', 'ER0', 'EH1', 'L', 'IY0')},
                    'ZUCCARO': {('Z', 'UW0', 'K', 'AA1', 'R', 'OW0')},
                    'ZUCCHINI': {('Z', 'UW0', 'K', 'IY1', 'N', 'IY0')},
                    'ZUCCO': {('Z', 'UW1', 'K', 'OW0')},
                    'ZUCH': {('Z', 'AH1', 'CH')},
                    'ZUCHOWSKI': {('Z', 'UW0', 'K', 'AO1', 'F', 'S', 'K', 'IY0'), ('Z', 'AH0', 'HH', 'AO1', 'F', 'S', 'K', 'IY0')},
                    'ZUCK': {('Z', 'AH1', 'K')},
                    'ZUCKER': {('Z', 'AH1', 'K', 'ER0'), ('Z', 'UW1', 'K', 'ER0')},
                    'ZUCKERMAN': {('Z', 'AH1', 'K', 'ER0', 'M', 'AH0', 'N'), ('Z', 'UW1', 'K', 'ER0', 'M', 'AH0', 'N')},
                    "ZUCKERMAN'S": {('Z', 'AH1', 'K', 'ER0', 'M', 'AH0', 'N', 'Z'), ('Z', 'UW1', 'K', 'ER0', 'M', 'AH0', 'N', 'Z')},
                    "ZUCKER'S": {('Z', 'AH1', 'K', 'ER0', 'Z')}}
        self.assertEqual(result, expected)

    def test_dict_invert_with_list(self):
        input_list = [
            ('ZUCCARELLI', 1, ['Z', 'UW0', 'K', 'ER0', 'EH1', 'L', 'IY0']),
            ('ZUCCARO', 1, ['Z', 'UW0', 'K', 'AA1', 'R', 'OW0']),
            ('ZUCCHINI', 1, ['Z', 'UW0', 'K', 'IY1', 'N', 'IY0']),
            ('ZUCCO', 1, ['Z', 'UW1', 'K', 'OW0']),
            ('ZUCH', 1, ['Z', 'AH1', 'CH']),
            ('ZUCHOWSKI', 1, ['Z', 'AH0', 'HH', 'AO1', 'F', 'S', 'K', 'IY0']),
            ('ZUCHOWSKI', 2, ['Z', 'UW0', 'K', 'AO1', 'F', 'S', 'K', 'IY0']),
            ('ZUCK', 1, ['Z', 'AH1', 'K']),
            ('ZUCKER', 1, ['Z', 'AH1', 'K', 'ER0']),
            ('ZUCKER', 2, ['Z', 'UW1', 'K', 'ER0']),
            ('ZUCKERMAN', 1, ['Z', 'AH1', 'K', 'ER0', 'M', 'AH0', 'N']),
            ('ZUCKERMAN', 2, ['Z', 'UW1', 'K', 'ER0', 'M', 'AH0', 'N']),
            ('ZUCKERMAN\'S', 1, ['Z', 'AH1', 'K', 'ER0', 'M', 'AH0', 'N', 'Z']),
            ('ZUCKERMAN\'S', 2, ['Z', 'UW1', 'K', 'ER0', 'M', 'AH0', 'N', 'Z']),
            ('ZUCKER\'S', 1, ['Z', 'AH1', 'K', 'ER0', 'Z'])
        ]
        result = dict_invert(input_list)
        expected = {1: {('ZUCCO', ('Z', 'UW1', 'K', 'OW0')),
                        ('ZUCK', ('Z', 'AH1', 'K')),
                        ('ZUCCHINI', ('Z', 'UW0', 'K', 'IY1', 'N', 'IY0')),
                        ('ZUCCARO', ('Z', 'UW0', 'K', 'AA1', 'R', 'OW0')),
                        ('ZUCCARELLI', ('Z', 'UW0', 'K', 'ER0', 'EH1', 'L', 'IY0')),
                        ('ZUCH', ('Z', 'AH1', 'CH')),
                        ("ZUCKER'S", ('Z', 'AH1', 'K', 'ER0', 'Z'))},
                    2: {('ZUCKERMAN', ('Z', 'UW1', 'K', 'ER0', 'M', 'AH0', 'N')),
                        ('ZUCKER', ('Z', 'UW1', 'K', 'ER0')),
                        ('ZUCHOWSKI', ('Z', 'AH0', 'HH', 'AO1', 'F', 'S', 'K', 'IY0')),
                        ("ZUCKERMAN'S", ('Z', 'AH1', 'K', 'ER0', 'M', 'AH0', 'N', 'Z')),
                        ("ZUCKERMAN'S", ('Z', 'UW1', 'K', 'ER0', 'M', 'AH0', 'N', 'Z')),
                        ('ZUCKER', ('Z', 'AH1', 'K', 'ER0')),
                        ('ZUCKERMAN', ('Z', 'AH1', 'K', 'ER0', 'M', 'AH0', 'N')),
                        ('ZUCHOWSKI', ('Z', 'UW0', 'K', 'AO1', 'F', 'S', 'K', 'IY0'))}}
        self.assertEqual(result, expected)
if __name__ == '__main__':
    unittest.main()