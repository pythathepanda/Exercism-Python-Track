def distance(strand_a, strand_b):
    """This is used to calculate the hamming distance between DNA"""
    if len(strand_a) != len(strand_b):
       raise ValueError("Strands must be of equal length.")
    hamming_distance = 0
    for index, chromosome in enumerate(strand_a):
        if chromosome != strand_b[index]:
            hamming_distance += 1
    
    return hamming_distance
