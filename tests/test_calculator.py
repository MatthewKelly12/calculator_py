import unittest
import sys
sys.path.append('../')
from calculator import Calculator
from decimal import Decimal


def setUpModule():
  print('set up module')

def tearDownModule():
  print('tear down module')

class TestCalculator(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    print('Set up class')
    # Create an instance of the calculator that can be used in all tests

  @classmethod
  def tearDownClass(self):
    print('Tear down class')

  def test_add(self):
    calc = Calculator()
    self.assertEqual(calc.add(2, 7), 9)
    self.assertEqual(calc.add(-2, -10), -12)

  def test_subtract(self):
      calc = Calculator()
      self.assertEqual(calc.subtract(2, 10), -8)
      self.assertEqual(calc.subtract(-2, -10), 8)

  def test_multiply(self):
      calc = Calculator()
      self.assertEqual(calc.multiply(2, 10), 20)
      self.assertEqual(calc.multiply(2, -10), -20)

  def test_divide(self):
      calc = Calculator()
      self.assertEqual(calc.divide(100, 50), 2)
      self.assertEqual(calc.divide(100, -50), -2)

  # Write test methods for subtract, multiply, and divide

if __name__ == '__main__':
    unittest.main()