def simple_moving_average(values, window_size):
    n = len(values)
    if window_size > n or window_size <= 0:
        return []
    
    result = []

    window_sum = sum(values[:window_size])
    result.append(window_sum / window_size)

    for i in range(window_size, n):
        window_sum += values[i]       
        window_sum -= values[i - window_size] 
        result.append(window_sum / window_size)
    
    return result