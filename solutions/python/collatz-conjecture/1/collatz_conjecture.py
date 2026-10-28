def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    counter = 0
    while number != 1:
        remainder = number % 2

        if remainder == 0:
            number = number / 2
            counter += 1
            continue

        if remainder == 1:
            number = number * 3
            number += 1
            counter += 1
            continue

    return counter