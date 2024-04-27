import unittest
from test import (
    get_position, compare_char, compare_str, type_by_angles, type_by_sides,
    convert_to_column, number_of_sentences, replace_with_stars, decrypt_message,
    exclude_letters, create_string, get_letters, find_intersection, find_union,
    number_of_occurence, number_of_capital_letters, polynomial_eval, pattern_number,
    one_swap_sorting, numbers_Ulam, happy_number, sum_of_divisors, turn_over
)

class TestFunctions(unittest.TestCase):
    def test_get_position(self):
        self.assertEqual(get_position('A'), 1)
        self.assertEqual(get_position('z'), 26)
        self.assertIsNone(get_position('Dj'))
        self.assertIsNone(get_position(1))

    def test_compare_char(self):
        self.assertFalse(compare_char('a', 'z'))
        self.assertTrue(compare_char('c', 'B'))
        self.assertIsNone(compare_char('d', 'ad'))
        self.assertIsNone(compare_char('2', 2))
        self.assertIsNone(compare_char('sdads', 'TEs'))

    def test_compare_str(self):
        self.assertFalse(compare_str('abc', 'Abd'))
        self.assertTrue(compare_str('zaD', 'zab'))
        self.assertFalse(compare_str('zaD', 'Zad'))
        self.assertIsNone(compare_str('aaa', 'aaaaa'))
        self.assertIsNone(compare_str('2015', 2015))

    def test_type_by_angles(self):
        self.assertEqual(type_by_angles(60, 60, 60), 'acute triangle')
        self.assertEqual(type_by_angles(90, 30, 60), 'right angled triangle')
        self.assertIsNone(type_by_angles(2015, 2015, 2015))
        self.assertIsNone(type_by_angles(90, 0, 90))

    def test_convert_to_column(self):
        self.assertEqual(convert_to_column("Revenge is a dish that tastes best when served cold."), "revenge\nis\na\ndish\nthat\ntastes\nbest\nwhen\nserved\ncold")
        self.assertEqual(convert_to_column("Never hate your enemies. It affects your judgment."), "never\nhate\nyour\nenemies\nit\naffects\nyour\njudgment")
        self.assertIsNone(convert_to_column(2015))

    def test_number_of_sentences(self):
        self.assertEqual(number_of_sentences("Revenge is a dish that tastes best when served cold."), 1)
        self.assertEqual(number_of_sentences("Never hate your enemies. It affects your judgment."), 2)
        self.assertIsNone(number_of_sentences(2015))

    def test_replace_with_stars(self):
        self.assertEqual(replace_with_stars("Revenge is a dish that tastes best when served cold."), '****************************************************')
        self.assertEqual(replace_with_stars("Never hate your enemies. It affects your judgment."), '**************************************************')
        self.assertIsNone(replace_with_stars(2015))

    def test_decrypt_message(self):
        self.assertEqual(decrypt_message("Sfwfohf jt b ejti uibu ubtuft cftu xifo tfswfe dpme."), 'Revenge is a dish that tastes best when served cold.')
        self.assertEqual(decrypt_message("Ofwfs ibuf zpvs fofnjft. Ju bggfdut zpvs kvehnfou."), 'Never hate your enemies. It affects your judgment.')
        self.assertIsNone(decrypt_message(2015))

    def test_exclude_letters(self):
        self.assertEqual(exclude_letters("aaabb", "b"), 'aaa')
        self.assertEqual(exclude_letters("abcc", "cczzyy"), 'ab')
        self.assertIsNone(exclude_letters(2015, "sasd"))
    
    def test_create_string(self):
        self.assertEqual(create_string([0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'bcc')
        self.assertEqual(create_string([4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4]), 'aaaazzzz')
        self.assertIsNone(create_string([4, 0, 0, 0, 0, 0]))

    def test_get_letters(self):
        self.assertEqual(get_letters(0), None)
        self.assertEqual(get_letters(1), 'a')
        self.assertIsNone(get_letters(-2015))

    def test_find_intersection(self):
        self.assertEqual(find_intersection("aaabb", "bbbbccc"), 'b')
        self.assertEqual(find_intersection("aZAbc", "zzYYxp"), 'z')
        self.assertIsNone(find_intersection("sfdfsdf", 2015))

    def test_find_union(self):
        self.assertEqual(find_union("aaabb", "bbbbccc"), 'abc')
        self.assertEqual(find_union("aZAbc", "zzYYxp"), 'AYZabcpxz')
        self.assertIsNone(find_union("sfdfsdf", 2015))

    def test_number_of_occurence(self):
        self.assertEqual(number_of_occurence(["man", "girl", "women", "boy"], "m"), 2)
        self.assertEqual(number_of_occurence(["ab", "aba", "a", "b", "ba"], "ba"), 2)
        self.assertIsNone(number_of_occurence([1, 2, 2015, 1, 3], "1"))

    def test_number_of_capital_letters(self):
        self.assertEqual(number_of_capital_letters("ArithmeticError"), 2)
        self.assertEqual(number_of_capital_letters("EOFError"), 4)
        self.assertIsNone(number_of_capital_letters(1))

    def test_polynomial_eval(self):
        self.assertEqual(polynomial_eval([2, 3, 0, 4], 4), 180)
        self.assertEqual(polynomial_eval([6], 42), 6)
        self.assertEqual(polynomial_eval([6, -2, -20], -1), -12)
        self.assertEqual(polynomial_eval([6, 0, -8, 0, -8, 0], 2), 112)
        self.assertEqual(polynomial_eval([6, 0, -8, 0, -8, 0], 1), -10)
        self.assertEqual(polynomial_eval([6, 0, -8, 0, -8, 0], 0), 0)

    def test_pattern_number(self):
        self.assertEqual(pattern_number([]), None)
        self.assertEqual(pattern_number([42]), None)
        self.assertEqual(pattern_number([1, 2]), None)
        self.assertEqual(pattern_number([1, 1]), ([1], 2))
        self.assertEqual(pattern_number([1, 2, 1]), None)
        self.assertEqual(pattern_number([1, 2, 3, 1, 2, 3]), ([1, 2, 3], 2))
        self.assertEqual(pattern_number([1, 2, 3, 1, 2]), None)
        self.assertEqual(pattern_number([1, 2, 3, 1, 2, 3, 1]), None)
        self.assertEqual(pattern_number(list(range(10))*20), ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 20))
        self.assertEqual(pattern_number('мама'), ('ма', 2))
        self.assertEqual(pattern_number('барабан'), None)

    def test_one_swap_sorting(self):
        self.assertFalse(one_swap_sorting([0, 1, 2, 3]))
        self.assertFalse(one_swap_sorting([]))
        self.assertFalse(one_swap_sorting([42]))
        self.assertTrue(one_swap_sorting([3, 2]))
        self.assertFalse(one_swap_sorting([2, 2]))
        self.assertTrue(one_swap_sorting([5, 2, 3, 4, 1, 6]))
        self.assertTrue(one_swap_sorting([1, 2, 3, 5, 4]))

    def test_numbers_Ulam(self):
        self.assertEqual(numbers_Ulam(10), [1, 2, 3, 4, 6, 8, 11, 13, 16, 18])
        self.assertEqual(numbers_Ulam(2), [1, 2])
        self.assertEqual(numbers_Ulam(1), [1])

    def test_happy_number(self):
        self.assertTrue(happy_number(32))
        self.assertFalse(happy_number(33))

    def test_sum_of_divisors(self):
        self.assertEqual(sum_of_divisors(3, [2, 0, 1, 5]), 0)
        self.assertEqual(sum_of_divisors(5, [2, 0, 1, 5]), 5)
        self.assertEqual(sum_of_divisors(7, []), 0)

    def test_turn_over(self):
        self.assertEqual(turn_over(4, ['f', 'o', 'o', 't', 'b', 'a', 'l', 'l']), ['t', 'o', 'o', 'f', 'b', 'a', 'l', 'l'])
        self.assertEqual(turn_over(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [5, 4, 3, 2, 1, 6, 7, 8, 9, 10])
        self.assertEqual(turn_over(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        self.assertEqual(turn_over(-5, []), [])


if __name__ == '__main__':
    unittest.main()
