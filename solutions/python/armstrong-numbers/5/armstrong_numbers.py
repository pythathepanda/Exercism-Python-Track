def is_armstrong_number(number):
    #Turn the number into a string
    digits = str(number)

    #Get the length of the stringy-fied digits, that going to be the power
    power = len(digits)

    #Calculate the Armstong number
    total = sum(int(digit) ** power for digit in digits)

    return total == number


    
