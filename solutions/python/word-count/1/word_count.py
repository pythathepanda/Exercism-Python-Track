import re
"""Import the RegEx library"""
def count_words(sentence):
    """This is a function to count the words in a sentence"""
    words = (re.findall(r"[a-z\d]+'?[a-z\d]+|\d+|[a-z]", sentence.lower()))
    return {word : words.count(word) for word in words}
