


def is_rectangle(sides):
    # Check if the length of sides is exactly 4
    if len(sides) != 4:
        return False
    # Sort the sides to easily check for pairs
    sides.sort()
    # Check if the first two and the last two sides are equal
    return sides[0] == sides[1] and sides[2] == sides[3]




def is_square(sides):
    if len(sides) != 4:
        return False
    return all(x == sides[0] for x in sides)


# print(is_square([1,1,1,1]))

def is_triangle(sides):
    if len(sides) != 3:
        return False
    a,b,c = sides
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False
            

