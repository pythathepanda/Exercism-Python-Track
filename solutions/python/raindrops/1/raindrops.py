def convert(number):
    pling = "Pling"
    plang = "Plang"
    plong = "Plong"

    div_three = number % 3
    div_five = number % 5
    div_seven  = number % 7

    if div_three == div_five == div_seven == 0:
        return pling + plang + plong
    elif div_three == div_five == 0:
        return pling + plang
    elif div_three == div_seven == 0:
        return pling + plong
    elif div_five == div_seven == 0:
        return plang + plong
    elif div_three == 0:
        return pling
    elif div_five == 0:
        return plang
    elif div_seven == 0:
        return plong
    else:
        return str(number)