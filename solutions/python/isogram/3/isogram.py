def is_isogram(phrase):
    """This is used to determine if a phrase is an isogram"""
    cleaned_phrase = phrase.replace(" ","").replace("-","").lower()
    
    phrase_set = set()
    cleaned_list = list(cleaned_phrase)
    phrase_set.update(cleaned_list)
        
    if len(phrase_set) != len(cleaned_phrase):
        return False
    
    return True