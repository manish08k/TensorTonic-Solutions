def polynomial_features(values, degree):
    result = []
    
    for x in values:
        row = []
        for d in range(degree + 1):
            row.append(x ** d)
        result.append(row)
    
    return result