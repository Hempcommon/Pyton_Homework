import math


def square(side):
    area = side * side
    if not isinstance(side, int):
        area = math.ceil(area)
    return area


print(square(5))
print(square(2.5))
print(square(3.1))
