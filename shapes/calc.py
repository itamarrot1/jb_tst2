from .detect import is_rectangle,is_triangle
import math


class ShapeError(Exception):
    """Custom exception for invalid shapes."""
    pass



def rectangle_perimeter(rect):
    if not is_rectangle(rect):
        raise ShapeError("The provided shape is not a proper rectangle.")
    
    # Calculate the perimeter
    return 2 * (rect[0] + rect[2])  # Assuming rect is sorted: [a, a, b, b]
        
def rectangle_area(rect):
    if not is_rectangle(rect):
        raise ShapeError("The provided shape is not a proper rectangle.")
    
    # Assuming rect is in the form [length, length, width, width] after sorting
    return rect[0] * rect[2]  # Calculate area as length * width

        
def triangle_perimeter(sides):
    if not is_triangle(sides):
        raise ShapeError("The provided shape is not a proper triangle.")
    
    # Calculate perimeter as the sum of the sides
    return sum(sides)


def triangle_area(sides):
    if not is_triangle(sides):
        raise ShapeError("The provided shape is not a proper triangle.")
    
    a, b, c = sides
    s = (a + b + c) / 2  # Semi-perimeter
    
    # Calculate area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
