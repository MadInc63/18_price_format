import unittest
from format_price import format_price


class FormatPriceTestCase(unittest.TestCase):
    def test_integer(self):
        price = format_price('123456789')
        self.assertEqual(price, '123 456 789')

    def test_float_round_up(self):
        price = format_price('123456.789')
        self.assertEqual(price, '123 456.79')

    def test_float_round_down(self):
        price = format_price('123456.123')
        self.assertEqual(price, '123 456.12')

    def test_without_integer_before_dot(self):
        price = format_price('.123')
        self.assertEqual(price, '0.12')

    def test_without_integer_after_dot(self):
        price = format_price('123.')
        self.assertEqual(price, '123')

    def test_letters(self):
        price = format_price('abcdefg')
        self.assertEqual(price, None)

    def test_symbol(self):
        price = format_price('#$%^&*')
        self.assertEqual(price, None)

    def test_punctuation(self):
        price = format_price('123456,789')
        self.assertEqual(price, None)

    def test_punctuation_multiple_dot(self):
        price = format_price('123.456.789')
        self.assertEqual(price, None)

    def test_whitespace(self):
        price = format_price('123 456789')
        self.assertEqual(price, None)


if __name__ == '__main__':
    unittest.main()
