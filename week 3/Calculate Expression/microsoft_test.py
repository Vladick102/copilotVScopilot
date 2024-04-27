from microsoft_fixed_1 import calculate_expression

import unittest


class TestCalculateExpression(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate_expression("Скільки буде 8 відняти 3?"), 5)

    def test_multiplication_and_addition(self):
        self.assertEqual(
            calculate_expression("Скільки буде 7 додати 3 помножити на 5?"), 50
        )

    def test_complex_expression(self):
        self.assertEqual(
            calculate_expression("Скільки буде 10 поділити на -2 додати 11 мінус -3?"),
            9,
        )

    def test_invalid_expression(self):
        self.assertEqual(
            calculate_expression("Скільки буде 3 в кубі?"), "Неправильний вираз!"
        )

    def test_invalid_syntax(self):
        self.assertEqual(
            calculate_expression("Скільки буде 2 2 додати?"), "Неправильний вираз!"
        )

    def test_non_math_expression(self):
        self.assertEqual(
            calculate_expression("Скільки сезонів в році?"), "Неправильний вираз!"
        )

    def test_division_by_zero(self):
        self.assertEqual(
            calculate_expression("Скільки буде 10 поділити на 0?"),
            "Неправильний вираз!",
        )

    def test_brackets(self):
        self.assertEqual(
            calculate_expression("Скільки буде (2 додати 3) помножити на 4?"), 20
        )

    def test_exponentiation(self):
        self.assertEqual(
            calculate_expression("Скільки буде 3 в квадраті?"), "Неправильний вираз!"
        )

    def test_negative_result(self):
        self.assertEqual(calculate_expression("Скільки буде 5 відняти 8?"), -3)

    def test_large_result(self):
        self.assertEqual(
            calculate_expression("Скільки буде 1000 помножити на 1000?"), 1000000
        )

    def test_large_negative_result(self):
        self.assertEqual(
            calculate_expression("Скільки буде -1000 відняти 2000?"), -3000
        )

    def test_zero_result(self):
        self.assertEqual(calculate_expression("Скільки буде 0 помножити на 100?"), 0)

    def test_invalid_words(self):
        self.assertEqual(
            calculate_expression("Скільки буде 2 додати 10 помножити на 7?"),
            84,
        )

    def test_no_operations(self):
        self.assertEqual(calculate_expression("Скільки буде 3?"), "Неправильний вираз!")


if __name__ == "__main__":
    unittest.main()
