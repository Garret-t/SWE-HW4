import unittest
from fullname import gen_fullname

class TestFullName(unittest.TestCase):
    def test_correct(self):
        self.assertEqual(gen_fullname("John", "Doe"), "John Doe")

if __name__ == "__main__":
    unittest.main(verbosity=2)