import unittest
from shapes.calc import ShapeError
from shapes.complex import check_shape

class TestDetect(unittest.TestCase):

    def test_check_shape(self):
        shapes = [
            [2, 3, 2, 3],  # Valid rectangle
            [4, 4, 4, 4],  # Valid square
            [3, 4, 5],     # Valid triangle
            [1, 1, 2],     # Invalid triangle
            [2, 2, 2]      # Invalid (not 4 sides)
        ]
        
        unique_shapes, improper_shapes = check_shape(shapes, raise_on_error=False)
        self.assertEqual(len(unique_shapes), 3)  # 1 rectangle, 1 square, 1 triangle
        self.assertEqual(len(improper_shapes), 2)  # 2 improper shapes

        with self.assertRaises(ShapeError):
            check_shape([[1, 1, 1]], raise_on_error=True)  # Should raise for invalid triangle