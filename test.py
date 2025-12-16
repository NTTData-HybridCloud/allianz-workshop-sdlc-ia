import unittest
from main import add_numbers, subtract_numbers, divide_numbers

class TestAddNumbers(unittest.TestCase):
    def test_integers(self):
        self.assertEqual(add_numbers(5, 7), 12)
        self.assertEqual(add_numbers(0, 0), 0)
        self.assertEqual(add_numbers(-3, 10), 7)
        self.assertEqual(add_numbers(-5, -8), -13)

    def test_floats(self):
        self.assertAlmostEqual(add_numbers(2.5, 0.5), 3.0)
        self.assertAlmostEqual(add_numbers(-1.25, 1.25), 0.0)
        self.assertAlmostEqual(add_numbers(1e100, 1e100), 2e100)

    def test_type_errors(self):
        # Demonstrate behavior with non-numeric inputs (should raise TypeError)
        with self.assertRaises(TypeError):
            _ = add_numbers('a', 1)
        with self.assertRaises(TypeError):
            _ = add_numbers(None, 2)

class TestSubtractNumbers(unittest.TestCase):
    def test_integers(self):
        self.assertEqual(subtract_numbers(10, 3), 7)
        self.assertEqual(subtract_numbers(0, 0), 0)
        self.assertEqual(subtract_numbers(5, 10), -5)
        self.assertEqual(subtract_numbers(-3, -8), 5)
        self.assertEqual(subtract_numbers(-10, 5), -15)

    def test_floats(self):
        self.assertAlmostEqual(subtract_numbers(5.5, 2.5), 3.0)
        self.assertAlmostEqual(subtract_numbers(1.25, 1.25), 0.0)
        self.assertAlmostEqual(subtract_numbers(2e100, 1e100), 1e100)
        self.assertAlmostEqual(subtract_numbers(-3.7, 2.3), -6.0)

    def test_type_errors(self):
        # Demonstrate behavior with non-numeric inputs (should raise TypeError)
        with self.assertRaises(TypeError):
            _ = subtract_numbers('a', 1)
        with self.assertRaises(TypeError):
            _ = subtract_numbers(None, 2)
        with self.assertRaises(TypeError):
            _ = subtract_numbers(10, 'b')

class TestDivideNumbers(unittest.TestCase):
    def test_integers(self):
        self.assertEqual(divide_numbers(10, 2), 5.0)
        self.assertEqual(divide_numbers(20, 4), 5.0)
        self.assertEqual(divide_numbers(9, 3), 3.0)
        self.assertEqual(divide_numbers(-10, 2), -5.0)
        self.assertEqual(divide_numbers(-20, -4), 5.0)
        self.assertEqual(divide_numbers(15, -3), -5.0)

    def test_floats(self):
        self.assertAlmostEqual(divide_numbers(5.5, 2.0), 2.75)
        self.assertAlmostEqual(divide_numbers(7.5, 2.5), 3.0)
        self.assertAlmostEqual(divide_numbers(1.0, 3.0), 0.3333333333333333)
        self.assertAlmostEqual(divide_numbers(-6.5, 2.0), -3.25)
        self.assertAlmostEqual(divide_numbers(2e100, 2.0), 1e100)

    def test_division_by_zero(self):
        # Test that division by zero raises ZeroDivisionError
        with self.assertRaises(ZeroDivisionError) as context:
            _ = divide_numbers(10, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")
        
        with self.assertRaises(ZeroDivisionError):
            _ = divide_numbers(0, 0)
        
        with self.assertRaises(ZeroDivisionError):
            _ = divide_numbers(-5, 0)

    def test_type_errors(self):
        # Demonstrate behavior with non-numeric inputs (should raise TypeError)
        with self.assertRaises(TypeError):
            _ = divide_numbers('a', 1)
        with self.assertRaises(TypeError):
            _ = divide_numbers(None, 2)
        with self.assertRaises(TypeError):
            _ = divide_numbers(10, 'b')

if __name__ == '__main__':
    unittest.main()
