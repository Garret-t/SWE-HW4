import unittest
from average import avg

class TestAverage(unittest.TestCase):
    def test_empty(self):
        self.assertRaises(ZeroDivisionError, avg, [])

    def test_float_neg(self):
        self.assertEqual(avg([.5,-.5, 3]), 1.0)

    def test_args(self):
        self.assertRaises(TypeError, avg, 1, 2, 3)

if __name__ == "__main__":
    unittest.main(verbosity=2)