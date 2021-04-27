import unittest
from volume import cube_volume

class TestVolume(unittest.TestCase):
    def test_correct(self):
        self.assertEqual(cube_volume(1,2,1.5), 3.0)


if __name__ == '__main__':
    unittest.main(verbosity=2)