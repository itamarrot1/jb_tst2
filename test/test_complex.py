import unittest
from shapes.detect import is_rectangle, is_square, is_triangle

class TestComplex(unittest.TestCase):

    def test_is_rectangle(self):
        self.assertTrue(is_rectangle([2, 3, 2, 3]))
        self.assertTrue(is_rectangle([3, 2, 3, 2]))
        self.assertFalse(is_rectangle([1, 2, 3]))
        self.assertFalse(is_rectangle([2, 2, 2, 2, 2]))

    def test_is_square(self):
        self.assertTrue(is_square([4, 4, 4, 4]))
        self.assertFalse(is_square([4, 4, 4, 2]))

    def test_is_triangle(self):
        self.assertTrue(is_triangle([3, 4, 5]))
        self.assertFalse(is_triangle([1, 1, 2]))  # Not a valid triangle
        self.assertFalse(is_triangle([2, 2, 2, 2]))  # Not a triangle
