def is_isogram(phrase):
    cleaned_phrase = phrase.replace(" ","").replace("-","").lower()
    
    phrase_set = set()
    cleaned_list = []
    
    for index in range(len(cleaned_phrase)):
        cleaned_list.append(cleaned_phrase[index])
        
    phrase_set.update(cleaned_list)
        
    if len(phrase_set) != len(cleaned_phrase):
        return False
    
    return True