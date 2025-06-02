import unittest

def get_sq(x):
    return x ** 2

class TestGetSq(unittest.TestCase):

    def test_positive_number(self):
        self.assertEqual(get_sq(3), 9)
        self.assertEqual(get_sq(2.5), 6.25)

    def test_negative_number(self):
        self.assertEqual(get_sq(-3), 9)
        self.assertEqual(get_sq(-2.5), 6.25)

    def test_zero(self):
        self.assertEqual(get_sq(0), 0)

if __name__ == "__main__":
    unittest.main()