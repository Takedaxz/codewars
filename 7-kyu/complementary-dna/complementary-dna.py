def DNA_strand(dna):
    # code here
    revert=""
    dna_map={"A":"T","T":"A","C":"G","G":"C"}
    for char in dna:
        revert+=dna_map[char]
        
    return revert