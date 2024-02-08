import unittest
from .even_numb import even_numbers


class Test(unittest.TestCase):
    def test_even_number_2(self):
        result = even_numbers(2)
        self.assertEqual(result, 'Число парне')
        self.assertNotEqual(result, 'Число не парне')
        self.assertIsInstance(result, str)

    def test_even_number_5(self):
        result = even_numbers(5)
        self.assertEqual(result, 'Число не парне')
        self.assertNotEqual(result, 'Число парне')
        self.assertIsInstance(result, str)

    def test_even_number_2222222(self):
        result = even_numbers(2222222)
        self.assertEqual(result, 'Число парне')
        self.assertNotEqual(result, 'Число не парне')
        self.assertIsInstance(result, str)
