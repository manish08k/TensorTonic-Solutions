def weighted_moving_average(values, weights):
    k = len(weights)
    w_sum = sum(weights)
    result = []
    
    for i in range(len(values) - k + 1):
        weighted_sum = 0
        for j in range(k):
            weighted_sum += values[i + j] * weights[j]
        
        result.append(weighted_sum / w_sum)
    
    return result