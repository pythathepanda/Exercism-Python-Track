def score(x_coordinate,y_coordinate):
    
    radius = calculate_radius(x_coordinate,y_coordinate)
    
    if 0 <= radius <= 1:
        return 10
    if 1 < radius <= 5:
        return 5
    if 5 < radius <= 10:
        return 1
    return 0

def calculate_radius(x_coordinate,y_coordinate):
    radius_squared = (x_coordinate ** 2) + (y_coordinate ** 2)
    radius = radius_squared ** (1 / 2)
    return radius
