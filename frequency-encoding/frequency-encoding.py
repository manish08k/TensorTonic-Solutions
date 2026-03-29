def frequency_encoding(values):
    n = len(values)
    
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    
    return [freq[v] / n for v in values]