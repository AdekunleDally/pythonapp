import unittest
from app import add_numbers


class TestAddNumbers(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_zero(self):
        self.assertEqual(add_numbers(0, 0), 0)


if __name__ == "__main__":
    unittest.main()
