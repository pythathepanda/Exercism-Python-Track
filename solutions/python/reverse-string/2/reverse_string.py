def reverse(text):
    """This is used to reverse a given string"""
    string_to_list = []
    reversed_word = ""
    
    for letter in range(len(text)):
        string_to_list.append(text[letter])
    
    string_to_list.reverse()
    
    for letter in range(len(text)):
        reversed_word += string_to_list[letter]
        
    return reversed_word
