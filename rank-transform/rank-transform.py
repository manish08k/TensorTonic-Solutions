def rank_transform(values):
    """
    Replace each value with its average rank.
    """
    n = len(values)
    
    # Pair each value with its index
    arr = [(val, i) for i, val in enumerate(values)]
    
    # Sort by value
    arr.sort()
    
    ranks = [0.0] * n
    i = 0
    
    while i < n:
        j = i
        
        # Find range of equal values
        while j < n and arr[j][0] == arr[i][0]:
            j += 1
        
        # Compute average rank (1-based indexing)
        avg_rank = (i + 1 + j) / 2.0
        
        # Assign rank to all tied values
        for k in range(i, j):
            _, idx = arr[k]
            ranks[idx] = avg_rank
        
        i = j
    
    return ranks