def convert(number):
    pling = "Pling"
    plang = "Plang"
    plong = "Plong"

    result = ""

    if number % 3 == 0: #Checks if divisible by 3
        result += pling # if yes, concatanate pling to string if no, skips to line 10
    if number % 5 == 0: #Checks if divisible by 5
        result += plang # if yes, concatanate plang to string if no, skips to line 10
    if number % 7 == 0: #Checks if divisible by 7
        result += plong # if yes, concatanate plong to string if no, skips to line 10

    return result if result else str (number) #returns result but if it's something else then                                                        str(number) 