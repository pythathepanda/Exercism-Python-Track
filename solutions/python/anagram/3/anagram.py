def find_anagrams(word, candidates):
    """A function to determine anagrams"""
    return [
        lang_unit
        for lang_unit in candidates
        if lang_unit.casefold() != word.casefold()
        and sorted(lang_unit.casefold()) == sorted(word.casefold())
    ]
    
