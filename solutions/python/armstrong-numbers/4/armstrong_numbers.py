def is_armstrong_number(number):
    # number is turned into a string
    number = str(number)
    
    #list to hold the stringified numbers
    number_to_string = []
    
    #variable to hold the armstrong number
    armstrong_number = 0
    
    #variable to hold the length of the number
    length_of_number = len(number)
    
    #Too loop through the stringified number
    for numb in range(len(number)):
        
        # append the number to the list
        number_to_string.append(number[numb])
        
        # turn each number to int 
        number_to_int = int(number[numb])
        
        # armstrong calculation
        armstrong_number += (number_to_int ** length_of_number)
        
    
    number = int(number)
    print(type(number))
    if armstrong_number == number:
        return True    
    
    return False


    
