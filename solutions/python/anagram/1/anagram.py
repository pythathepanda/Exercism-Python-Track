def find_anagrams(word, candidates):
    """This is a function to find anagrams"""
    anagram_list = []
    word_lower = word.lower()
    
    for index, candidate in enumerate(candidates):
        candidate_lower = candidate.lower()
        
        if len(candidate) != len(word) or candidate_lower == word_lower:
            continue
        
        is_anagram = True
        
        for letter in word_lower:
            if word_lower.count(letter) != candidate_lower.count(letter):
                is_anagram = False
                break
            
        if is_anagram:
            anagram_list.append(candidate)
            
    return anagram_list
