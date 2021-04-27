import unittest
from volume import cube_volume

class TestVolume(unittest.TestCase):
    def test_float(self):
        self.assertEqual(cube_volume(1,2,1.5), 3.0)

    def test_negative(self):
        self.assertNotEqual(cube_volume(-1,2,3), -6)

    def test_type(self):
        self.assertRaises(TypeError, cube_volume, 'A', '2b', 3)
    
if __name__ == '__main__':
    unittest.main(verbosity=2)