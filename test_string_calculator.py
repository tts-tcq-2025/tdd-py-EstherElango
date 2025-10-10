# test_string_calculator.py
import unittest
from string_calculator import add


class TestStringCalculator(unittest.TestCase):

    def test_empty_string_returns_zero(self):
        self.assertEqual(add(""), 0)

    def test_single_number(self):
        self.assertEqual(add("1"), 1)
        self.assertEqual(add("7"), 7)

    def test_two_numbers_comma(self):
        self.assertEqual(add("1,2"), 3)
        self.assertEqual(add("10,20"), 30)

    def test_unknown_amount_of_numbers(self):
        self.assertEqual(add("1,2,3,4,5"), 15)
        self.assertEqual(add("10,20,30,40"), 100)

    def test_newline_as_delimiter(self):
        self.assertEqual(add("1\n2,3"), 6)

    def test_custom_single_char_delimiter(self):
        self.assertEqual(add("//;\n1;2"), 3)
        self.assertEqual(add("//-\n5-6-7"), 18)

    def test_delimiter_of_any_length(self):
        self.assertEqual(add("//[***]\n1***2***3"), 6)
        self.assertEqual(add("//[###]\n4###5###6"), 15)

    def test_multiple_delimiters(self):
        self.assertEqual(add("//[*][%]\n1*2%3"), 6)
        self.assertEqual(add("//[**][%%]\n10**20%%30"), 60)

    def test_ignore_numbers_greater_than_1000(self):
        self.assertEqual(add("2,1001"), 2)
        self.assertEqual(add("1000,2"), 1002)

    def test_negative_number_throws_exception(self):
        with self.assertRaisesRegex(ValueError, r"negatives not allowed: -2"):
            add("1,-2,3")

    def test_multiple_negatives_show_all_in_exception(self):
        with self.assertRaisesRegex(ValueError, r"negatives not allowed: -1, -5"):
            add("-1,-5,7")

    def test_invalid_tokens_raise(self):
        # "1,\n" is considered invalid (empty token) and should raise
        with self.assertRaises(ValueError):
            add("1,\n")


if __name__ == "__main__":
    unittest.main()
