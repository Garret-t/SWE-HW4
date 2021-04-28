import unittest
from fullname import gen_fullname

class TestFullName(unittest.TestCase):
    def test_correct(self):
        self.assertEqual(gen_fullname("John", "Doe"), "John Doe")

    def test_empty(self):
        self.assertNotEqual(gen_fullname("", ""), " ")

    def test_letters(self):
        self.assertRegex(gen_fullname("John", "Doe"), "[a-zA-Z][a-zA-Z ]+[a-zA-Z]$")
    
    def test_symbols(self):
        self.assertRegex(gen_fullname("J0hn", "Do3"), "[a-zA-Z][a-zA-Z ]+[a-zA-Z]$")
    

if __name__ == "__main__":
    unittest.main(verbosity=2)