import unittest
from demo import add_numbers

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

if __name__ == '__main__':
    unittest.main()
