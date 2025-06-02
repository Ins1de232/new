import unittest

def is_even(number):
    return number % 2 == 0

class TestIsEven(unittest.TestCase):

    def test_even_numbers(self):
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(4))
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(-2))

    def test_odd_numbers(self):
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(-1))
        self.assertFalse(is_even(-3))

if __name__ == "__main__":
    unittest.main()
