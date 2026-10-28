def is_pangram(sentence):
    """This is used to check if a sentence is a pangram"""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = list(alphabet)
    print(alphabet)
    
    cleaned_sentence = sentence.replace(" ","").replace(".","").lower()
    cleaned_list = []
    
    for index, letter in enumerate(cleaned_sentence):
        check = letter.isalpha()
        if check is True:
            if letter not in cleaned_list:
                cleaned_list.append(cleaned_sentence[index])
            
    cleaned_list.sort()
    
    if cleaned_list == alphabet:
        return True
    
    return False
    

    