def score(x,y):
    
    radius = calculate_radius(x,y)
    
    if radius <= 1 and radius  >= 0:
        return 10
    if radius <= 5 and radius  > 1:
        return 5
    if radius <= 10 and radius > 5:
        return 1
    return 0

def calculate_radius(x,y):
    radius_squared = (x ** 2) + (y ** 2)
    radius = radius_squared ** (1 / 2)
    return radius
