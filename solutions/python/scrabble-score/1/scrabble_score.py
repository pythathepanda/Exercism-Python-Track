def score(word):
    """This is used to calculate your scrabble score"""
    score_mapping = {
        1 : ["A","E","I","O","U","N","L","R","S","T"],
        2 : ["D", "G"],
        3 : ["B","C","M","P"],
        4 : ["F","H","V","W","Y"],
        5 : ["K"],
        8 : ["J","X"],
        10 : ["Q","Z"]
    }
    player_score = 0
    
    word = word.upper()
    
    for letter in word:
        for key, content in score_mapping.items():
            if letter in content:
                player_score += key
        
    return player_score

