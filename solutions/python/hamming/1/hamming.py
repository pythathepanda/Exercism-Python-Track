def distance(strand_a, strand_b):
    #Iterate over strand_a and compare with strand_b
    if len(strand_a) != len(strand_b):
       raise ValueError("Strands must be of equal length.")
    hamming_distance = 0
    for ham in range(len(strand_a)):
        if strand_a[ham] != strand_b[ham]:
            hamming_distance += 1
    
    return hamming_distance
