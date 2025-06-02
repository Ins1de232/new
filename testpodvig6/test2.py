import unittest

def get_square(tp, *args):
    if tp == "RECT":
        length, width = args
        return length * width
    else:
        side = args[0]
        return side * side

class TestGetSquare(unittest.TestCase):

    def test_rectangle_area(self):
        self.assertEqual(get_square("RECT", 5, 10), 50)
        self.assertEqual(get_square("RECT", 2.5, 4), 10.0)

    def test_square_area(self):
        self.assertEqual(get_square("SQUARE", 4), 16)
        self.assertEqual(get_square("SQUARE", 3.5), 12.25)

if __name__ == "__main__":
    unittest.main()
