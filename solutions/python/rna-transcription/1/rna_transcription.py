def to_rna(dna_strand):
    """This is used to generate the rna_strand"""
    
    dna_strand = dna_strand.lower()
    rna_strand = ""
    
    for letter in dna_strand:
        if letter == "g":
            rna_strand += "c"
            
        if letter == "c":
            rna_strand += "g"
            
        if letter == "t":
            rna_strand += "a"
            
        if letter == "a":
            rna_strand += "u"
            
    
    rna_strand = rna_strand.upper()
    return(rna_strand)
    