def jaccard_similarity(set_a, set_b):
    A = set(set_a)
    B = set(set_b)
    
    # handle edge case
    if len(A) == 0 and len(B) == 0:
        return 0.0
    
    intersection = A & B
    union = A | B
    
    return len(intersection) / len(union)