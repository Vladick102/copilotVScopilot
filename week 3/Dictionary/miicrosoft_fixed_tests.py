import unittest
import tempfile
import os
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
class TestDictReaderTuple(unittest.TestCase):
    def setUp(self):
        # Create a temporary file with sample dictionary content
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file.write(b"NACHOS 1 N AA1 CH OW0 Z")
        self.temp_file.close()

    def tearDown(self):
        # Clean up the temporary file
        os.remove(self.temp_file.name)

    def test_single_pronunciation(self):
        # Test a word with a single pronunciation
        result = dict_reader_tuple(self.temp_file.name)
        self.assertEqual(result, [("NACHOS", 1, ["N", "AA1", "CH", "OW0", "Z"])])

    def test_multiple_pronunciations(self):
        # Test a word with multiple pronunciations
        file_content = "ZSCHAU 1 ZH AW1.\nZUBA 1 Z UW1 B AH0\nZUBE 1 Z UW1 B"
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(file_content.encode())
            temp_file.close()
            result = dict_reader_tuple(temp_file.name)
            expected = [
                ("ZSCHAU", 1, ["ZH", "AW1."]),
                ("ZUBA", 1, ["Z", "UW1", "B", "AH0"]),
                ("ZUBE", 1, ["Z", "UW1", "B"])
            ]
            self.assertEqual(result, expected)

    def test_empty_input(self):
        # Test an empty input
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.close()
            result = dict_reader_tuple(temp_file.name)
            self.assertEqual(result, [])

    def test_invalid_input(self):
        # Test an invalid input
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(b"INVALID")
            temp_file.close()
            result = dict_reader_tuple(temp_file.name)
            self.assertEqual(result, [])

    def test_same_word_different_pronunciation(self):
        # Test the same word with different pronunciations
        file_content = "NACHOS 1 N AA1 CH OW0 Z\nNACHOS 2 N AE1 CH OW0 Z"
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(file_content.encode())
            temp_file.close()
            result = dict_reader_tuple(temp_file.name)
            expected = [
                ("NACHOS", 1, ["N", "AA1", "CH", "OW0", "Z"]),
                ("NACHOS", 2, ["N", "AE1", "CH", "OW0", "Z"])
            ]
            self.assertEqual(result, expected)

    def test_single_pronunciation_dict(self):
        # Test a word with a single pronunciation
        result = dict_reader_dict(self.temp_file.name)
        expected = {"NACHOS": {("N", "AA1", "CH", "OW0", "Z")}}
        self.assertEqual(result, expected)

    def test_multiple_pronunciations_dict(self):
        # Test a word with multiple pronunciations
        file_content = "ZSCHAU 1 ZH AW1.\nZUBA 1 Z UW1 B AH0\nZUBE 1 Z UW1 B"
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(file_content.encode())
            temp_file.close()
            result = dict_reader_dict(temp_file.name)
            expected = {
                "ZSCHAU": {("ZH", "AW1.")},
                "ZUBA": {("Z", "UW1", "B", "AH0")},
                "ZUBE": {("Z", "UW1", "B")}
            }
            self.assertEqual(result, expected)

    def test_empty_input_dict(self):
        # Test an empty input
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.close()
            result = dict_reader_dict(temp_file.name)
            self.assertEqual(result, {})

    def test_invalid_input_dict(self):
        # Test an invalid input
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(b"INVALID")
            temp_file.close()
            result = dict_reader_dict(temp_file.name)
            self.assertEqual(result, {})

    def test_same_word_different_pronunciation_dict(self):
        # Test the same word with different pronunciations
        file_content = "NACHOS 1 N AA1 CH OW0 Z\nNACHOS 2 N AE1 CH OW0 Z"
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(file_content.encode())
            temp_file.close()
            result = dict_reader_dict(temp_file.name)
            expected = {
                "NACHOS": {("N", "AA1", "CH", "OW0", "Z"), ("N", "AE1", "CH", "OW0", "Z")}
            }
            self.assertEqual(result, expected)

    def test_single_pronunciation_last(self):
        # Test a word with a single pronunciation
        input_dict = {'WATER': {('W', 'A', 'T', 'E', 'R')}}
        result = dict_invert(input_dict)
        expected = {1: {('WATER', ('W', 'A', 'T', 'E', 'R'))}}
        self.assertEqual(result, expected)

    def test_multiple_pronunciations_last(self):
        # Test a word with multiple pronunciations
        input_dict = {
            'AABERG': {('AA1', 'B', 'ER0', 'G')},
            'A.': {('EY1',)},
            'A': {('EY1',), ('AH0',)},
            'A42128': {('EY1', 'F', 'AO1', 'R', 'T', 'UW1', 'W', 'AH1', 'N', 'T', 'UW1', 'EY1', 'T')},
            'AAA': {('T', 'R', 'IH2', 'P', 'AH0', 'L', 'EY1')}
        }
        result = dict_invert(input_dict)
        expected = {
            1: {
                ('A.', ('EY1',)),
                ('AABERG', ('AA1', 'B', 'ER0', 'G')),
                ('AAA', ('T', 'R', 'IH2', 'P', 'AH0', 'L', 'EY1')),
                ('A42128', ('EY1', 'F', 'AO1', 'R', 'T', 'UW1', 'W', 'AH1', 'N', 'T', 'UW1', 'EY1', 'T'))
            },
            2: {
                ('A', ('EY1',)),
                ('A', ('AH0',))
            }
        }
        self.assertEqual(result, expected)

    def test_single_pronunciation_list(self):
        input_dict = {'WATER': {('W', 'A', 'T', 'E', 'R')}}
        result = dict_invert(input_dict)
        expected = {1: {('WATER', ('W', 'A', 'T', 'E', 'R'))}}
        self.assertEqual(result, expected)

    def test_multiple_pronunciations_list(self):
        input_dict = {
            'AABERG': {('AA1', 'B', 'ER0', 'G')},
            'A.': {('EY1',)},
            'A': {('EY1',), ('AH0',)},
            # Add more words and pronunciations here
        }
        result = dict_invert(input_dict)
        expected = {
            1: {('A.', ('EY1',)), ('AABERG', ('AA1', 'B', 'ER0', 'G'))},
            2: {('A', ('EY1',)), ('A', ('AH0',))},
            # Add more expected results for other words
        }
        self.assertEqual(result, expected)

    def test_single_item(self):
        input_list = [('WATER', 1, [('W', 'A', 'T', 'E', 'R')])]
        result = dict_invert(input_list)
        expected = {1: {('WATER', ('W', 'A', 'T', 'E', 'R'))}}
        self.assertEqual(result, expected)

    def test_multiple_items_same_key(self):
        input_list = [
            ('A', 1, [('X', 'Y', 'Z')]),
            ('A', 2, [('P', 'Q', 'R')]),
            ('A', 3, [('M', 'N', 'O')]),
        ]
        result = dict_invert(input_list)
        expected = {'A': {('X', 'Y', 'Z'), ('P', 'Q', 'R'), ('M', 'N', 'O')}}
        self.assertEqual(result, expected)

    def test_multiple_items_different_keys(self):
        input_list = [
            ('A', 1, [('X', 'Y', 'Z')]),
            ('B', 1, [('P', 'Q', 'R')]),
            ('C', 1, [('M', 'N', 'O')]),
        ]
        result = dict_invert(input_list)
        expected = {
            'A': {('X', 'Y', 'Z')},
            'B': {('P', 'Q', 'R')},
            'C': {('M', 'N', 'O')},
        }
        self.assertEqual(result, expected)

    

if __name__ == "__main__":
    unittest.main()

input_list = [('A', 1, ['X', 'Y', 'Z']), ('B', 1, ['P', 'Q', 'R'])]
print(dict_invert(input_list))