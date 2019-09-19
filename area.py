import math
def triangle_area(height, base):
    
    if base < 0 or height < 0:
        raise ValueError("Cannot have a negative value.")
    
    return height * base * 0.5

def circle_area(radius):
    if radius < 0:
        raise ValueError
    return radius ** 2 * math.pi