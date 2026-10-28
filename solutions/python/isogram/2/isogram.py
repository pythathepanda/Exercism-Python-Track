def is_isogram(phrase):
    cleaned_phrase = phrase.replace(" ","").replace("-","").lower()
    
    phrase_set = set()
    cleaned_list = list(cleaned_phrase)
    phrase_set.update(cleaned_list)
        
    if len(phrase_set) != len(cleaned_phrase):
        return False
    
    return True