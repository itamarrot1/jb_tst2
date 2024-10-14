from .detect import is_rectangle,is_triangle,is_square
from .calc import rectangle_area,rectangle_perimeter,triangle_area,ShapeError


def check_shape(shapes, raise_on_error=True):
    unique_shapes = {}
    improper_shapes = []

    for sides in shapes:
        sorted_sides = tuple(sorted(sides))  # Use a tuple to handle uniqueness
        if is_square(sides):
            if sorted_sides not in unique_shapes:
                unique_shapes[sorted_sides] = {
                    "shape": "square",
                    "perimeter": rectangle_perimeter(sides),
                    "area": rectangle_area(sides)
                }
        elif is_rectangle(sides):
            if sorted_sides not in unique_shapes:
                unique_shapes[sorted_sides] = {
                    "shape": "rectangle",
                    "perimeter": rectangle_perimeter(sides),
                    "area": rectangle_area(sides)
                }
        elif is_triangle(sides):
            if sorted_sides not in unique_shapes:
                area = triangle_area(sides)
                perimeter = sum(sides)
                unique_shapes[sorted_sides] = {
                    "shape": "triangle",
                    "area": area,
                    "perimeter": perimeter
                }
        else:
            improper_shapes.append(sides)
            if raise_on_error:
                raise ShapeError("The provided shape is not a proper shape: {}".format(sides))

    return unique_shapes, improper_shapes



shapes=[[2, 2, 2, 2], [3, 4, 5], [5, 6, 6], [2, 3, 2, 3], [2, 3, 8], [3, 4, 5]] 

print(check_shape(shapes,  raise_on_error=True))