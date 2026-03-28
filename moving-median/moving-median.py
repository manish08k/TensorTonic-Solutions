def moving_median(values, window_size):

    n = len(values)

    if window_size > n or window_size <= 0:
        return []
    
    result = []
    
    for i in range(n - window_size + 1):
        window = values[i:i + window_size]
        

        window.sort()
        
        if window_size % 2 == 1:
            median = float(window[window_size // 2])
        else:
            mid1 = window[window_size // 2 - 1]
            mid2 = window[window_size // 2]
            median = (mid1 + mid2) / 2.0
        
        result.append(median)
    
    return result