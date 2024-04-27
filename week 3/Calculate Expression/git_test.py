import unittest
from git_fixed import calculate_expression


class TestCalculateExpression(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate_expression("Скільки буде 5 додати 5?"), 10)

    def test_multiple_operations(self):
        self.assertEqual(
            calculate_expression("Скільки буде 2 помножити на 10 додати 7?"), 27
        )

    def test_no_operation_priority(self):
        self.assertEqual(
            calculate_expression("Скільки буде 2 додати 10 помножити на 7?"), 84
        )

    def test_subtraction(self):
        self.assertEqual(calculate_expression("Скільки буде 8 відняти 3?"), 5)

    def test_division(self):
        self.assertEqual(
            calculate_expression("Скільки буде 10 поділити на -2 додати 11 мінус -3?"),
            9,
        )

    def test_unsupported_operation(self):
        self.assertEqual(
            calculate_expression("Скільки буде 3 в кубі?"), "Неправильний вираз!"
        )

    def test_non_mathematical_expression(self):
        self.assertEqual(
            calculate_expression("Скільки сезонів в році?"), "Неправильний вираз!"
        )

    def test_incorrect_syntax(self):
        self.assertEqual(
            calculate_expression("Скільки буде 2 2 додати?"), "Неправильний вираз!"
        )

    def test_zero_operations(self):
        self.assertEqual(calculate_expression("Скільки буде 0 додати 0?"), 0)
        self.assertEqual(calculate_expression("Скільки буде 5 помножити на 0?"), 0)

    def test_negative_numbers(self):
        self.assertEqual(calculate_expression("Скільки буде -5 додати -5?"), -10)
        self.assertEqual(calculate_expression("Скільки буде -5 помножити на -5?"), 25)

    def test_division_by_zero(self):
        self.assertEqual(
            calculate_expression("Скільки буде 5 поділити на 0?"), "Неправильний вираз!"
        )

    def test_empty_expression(self):
        self.assertEqual(calculate_expression(""), "Неправильний вираз!")

    def test_whitespace_in_expression(self):
        self.assertEqual(calculate_expression(" Скільки буде 5 додати 5? "), 10)
        self.assertEqual(calculate_expression("Скільки буде 5 додати 5 ?"), 10)

    def test_large_numbers(self):
        self.assertEqual(
            calculate_expression("Скільки буде 1000000 додати 1000000?"), 2000000
        )
        self.assertEqual(
            calculate_expression("Скільки буде 1000000 помножити на 1000000?"),
            1000000000000,
        )

    def test_multiple_spaces(self):
        self.assertEqual(calculate_expression("Скільки  буде  5  додати  5?"), 10)

    def test_unexpected_characters(self):
        self.assertEqual(
            calculate_expression("Скільки буде 5 додати 5?!"), "Неправильний вираз!"
        )
        self.assertEqual(
            calculate_expression("Скільки буде 5 додати 5#?"), "Неправильний вираз!"
        )

    def test_decimal_numbers(self):
        self.assertEqual(
            calculate_expression("Скільки буде 5.5 додати 5.5?"), "Неправильний вираз!"
        )

    def test_missing_numbers(self):
        self.assertEqual(
            calculate_expression("Скільки буде додати 5?"), "Неправильний вираз!"
        )
        self.assertEqual(
            calculate_expression("Скільки буде 5 додати?"), "Неправильний вираз!"
        )

    def test_missing_operation(self):
        self.assertEqual(
            calculate_expression("Скільки буде 5 5?"), "Неправильний вираз!"
        )

    def test_multiple_operations_without_numbers(self):
        self.assertEqual(
            calculate_expression("Скільки буде додати додати?"), "Неправильний вираз!"
        )

    def test_unexpected_order(self):
        self.assertEqual(
            calculate_expression("? Скільки буде 5 додати 5"), "Неправильний вираз!"
        )
        self.assertEqual(
            calculate_expression("Скільки буде ? 5 додати 5"), "Неправильний вираз!"
        )

    def test_unexpected_symbols(self):
        self.assertEqual(
            calculate_expression("Скільки буде 5 додати 5?!!"), "Неправильний вираз!"
        )
        self.assertEqual(
            calculate_expression("Скільки буде 5 додати 5?#"), "Неправильний вираз!"
        )

    def test_multiple_questions(self):
        self.assertEqual(
            calculate_expression("Скільки буде 5 додати 5? Скільки буде 2 додати 2?"),
            "Неправильний вираз!",
        )

    def test_no_space_after_question(self):
        self.assertEqual(
            calculate_expression("Скільки буде 5 додати 5?Скільки буде 2 додати 2?"),
            "Неправильний вираз!",
        )

    def test_no_space_before_question(self):
        self.assertEqual(
            calculate_expression("Скільки буде 5 додати 5?Скільки буде 2 додати 2?"),
            "Неправильний вираз!",
        )

    def test_no_space_between_numbers_and_operations(self):
        self.assertEqual(
            calculate_expression("Скільки буде 5додати5?"), "Неправильний вираз!"
        )

    def test_no_space_between_operations_and_numbers(self):
        self.assertEqual(
            calculate_expression("Скільки буде 5 додати5?"), "Неправильний вираз!"
        )

    def test_only_question(self):
        self.assertEqual(calculate_expression("?"), "Неправильний вираз!")

    def test_only_operation(self):
        self.assertEqual(
            calculate_expression("Скільки буде додати?"), "Неправильний вираз!"
        )

    def test_only_numbers(self):
        self.assertEqual(
            calculate_expression("Скільки буде 5 5?"), "Неправильний вираз!"
        )

    def test_duplicate_operations(self):
        self.assertEqual(
            calculate_expression("Скільки буде 5 додати додати 5?"),
            "Неправильний вираз!",
        )

    def test_duplicate_numbers(self):
        self.assertEqual(
            calculate_expression("Скільки буде 5 5 додати?"), "Неправильний вираз!"
        )

    def test_extra_spaces(self):
        self.assertEqual(calculate_expression(" Скільки  буде  5  додати  5 ? "), 10)

    def test_case_sensitivity(self):
        self.assertEqual(calculate_expression("СКІЛЬКИ БУДЕ 5 ДОДАТИ 5?"), 10)


if __name__ == "__main__":
    unittest.main()
