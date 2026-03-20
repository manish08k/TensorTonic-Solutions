def elu(x_list, alpha):
    result = []
    for x in x_list:
        if x > 0:
            result.append(x)
        else:
            result.append(alpha * (math.exp(x) - 1))
    return result

# Example
print(elu([1.0, -1.0, 0.0, 2.0, -0.5], 1.0))