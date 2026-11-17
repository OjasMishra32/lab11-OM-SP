# https://github.com/OjasMishra32/lab11-OM-SP
# Partner 1: Ojasva Mishra
# Partner 2: Shrish Panchedhri

import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-4, 2), -2)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(8, 3), 5)
        self.assertEqual(subtract(2, 7), -5)
        self.assertEqual(subtract(-3, -3), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 7), 0)

    def test_divide(self):
        self.assertEqual(divide(2, 8), 4)
        self.assertEqual(divide(-3, 9), -3)
        self.assertAlmostEqual(divide(3, 1), 1 / 3)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, -4)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(3, 1), 0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 5)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(-3, -4), 5)
        self.assertEqual(hypotenuse(0, 0), 0)

    def test_sqrt(self):
        self.assertEqual(square_root(25), 5)
        self.assertAlmostEqual(square_root(2), 1.4142135623730951)
        with self.assertRaises(ValueError):
            square_root(-9)


if __name__ == "__main__":
    unittest.main()
