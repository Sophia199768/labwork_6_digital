import unittest
from calc import calc

class calculator_tests(unittest.TestCase):

  def setUp(self):
    self.calculator = calc()

  def test_sum(self):
    self.assertEqual(self.calculator.sum(5, 7), 12)

  def test_subtract(self):
    self.assertEqual(self.calculator.subtract(17, 7), 10)

  def test_multiply(self):
    self.assertEqual(self.calculator.multiply(7, 8), 56)

  def test_divide(self):
    self.assertEqual(self.calculator.divide(10, 2), 5)

  def test_divide(self):
    self.assertEqual(self.calculator.divide(10, 0), "Error")

if __name__ == "__main__":
  unittest.main()