import unittest
from average import avg

class TestAverage(unittest.TestCase):
    def test_empty(self):
        self.assertRaises(ZeroDivisionError, avg, [])
    
if __name__ == "__main__":
    unittest.main(verbosity=2)