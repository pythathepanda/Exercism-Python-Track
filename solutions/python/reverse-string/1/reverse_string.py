def reverse(text):
    """This is used to reverse a given string"""
    string_to_list = []
    reversed_word = ""
    
    for index, letter in enumerate(text):
        string_to_list.append(letter)
    
    string_to_list.reverse()
    
    for index, letter in enumerate(string_to_list):
        reversed_word += letter
        
    return reversed_word
