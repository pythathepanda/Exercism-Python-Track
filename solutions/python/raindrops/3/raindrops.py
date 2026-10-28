def convert(number):
    pling = "Pling"
    plang = "Plang"
    plong = "Plong"

    div_three = number % 3
    div_five = number % 5
    div_seven  = number % 7

    if div_three == div_five == div_seven == 0:
        return pling + plang + plong
        
    if div_three == div_five == 0:
        return pling + plang
        
    if div_three == div_seven == 0:
        return pling + plong
        
    if div_five == div_seven == 0:
        return plang + plong
        
    if div_three == 0:
        return pling
        
    if div_five == 0:
        return plang
        
    if div_seven == 0:
        return plong
        
    return str(number)