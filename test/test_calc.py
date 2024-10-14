import unittest
from shapes.calc import rectangle_perimeter, rectangle_area, triangle_area
from shapes.detect import ShapeError

class TestCalc(unittest.TestCase):

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle_perimeter([2, 3, 2, 3]), 10)
        self.assertEqual(rectangle_perimeter([1, 1, 1, 1]), 4)

    def test_rectangle_area(self):
        self.assertEqual(rectangle_area([2, 3, 2, 3]), 6)
        self.assertEqual(rectangle_area([1, 1, 1, 1]), 1)

    def test_triangle_area(self):
        self.assertAlmostEqual(triangle_area([3, 4, 5]), 6)
        self.assertAlmostEqual(triangle_area([5, 5, 6]), 12)