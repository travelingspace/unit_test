def triangle_area(height, base):
    
    if base < 0 or height < 0:
        raise ValueError("Cannot have a negative value.")
    
    return height * base * 0.5