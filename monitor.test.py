import unittest
from string_calculator import add, extract_header_and_body, get_delimiters, token_to_int


class TestStringCalculator(unittest.TestCase):

    def test_empty_string_returns_zero(self):
        self.assertEqual(add(""), 0)

    def test_single_number(self):
        self.assertEqual(add("1"), 1)

    def test_two_numbers_comma(self):
        self.assertEqual(add("1,2"), 3)

    def test_multiple_numbers(self):
        self.assertEqual(add("1,2,3,4,5"), 15)

    def test_newline_as_delimiter(self):
        self.assertEqual(add("1\n2,3"), 6)

    def test_custom_delimiter(self):
        self.assertEqual(add("//;\n1;2"), 3)

    def test_custom_delimiter_with_brackets(self):
        self.assertEqual(add("//[***]\n1***2***3"), 6)

    def test_numbers_above_1000_are_ignored(self):
        self.assertEqual(add("2,1001,3"), 5)

    def test_negative_number_raises_error(self):
        with self.assertRaises(ValueError) as e:
            add("1,-2,3,-4")
        self.assertIn("negatives not allowed", str(e.exception))
        self.assertIn("-2", str(e.exception))
        self.assertIn("-4", str(e.exception))

    def test_invalid_number_token_raises_error(self):
        with self.assertRaises(ValueError):
            add("1,,2")  # empty token between commas

    def test_invalid_delimiter_header_raises_error(self):
        with self.assertRaises(ValueError):
            get_delimiters("[")  # malformed header

    def test_extract_header_without_newline_raises_error(self):
        with self.assertRaises(ValueError):
            extract_header_and_body("//;1;2")  # no newline

    def test_token_to_int_invalid_string(self):
        with self.assertRaises(ValueError):
            token_to_int("abc")


if __name__ == "__main__":
    unittest.main()
