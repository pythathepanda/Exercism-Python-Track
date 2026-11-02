def transform(legacy_data):
    """This is a function to transform legacy data"""
    new_data = {}
    
    for key, content in legacy_data.items():
        for letter in content:
            new_data[letter.lower()] = key
            
    return new_data
