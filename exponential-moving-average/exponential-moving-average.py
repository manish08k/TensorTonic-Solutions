def exponential_moving_average(values, alpha):

    n = len(values)
    if n == 0:
        return []
    ema = [0.0] * n
    ema[0] = float(values[0])
    for t in range(1, n):
        ema[t] = alpha * values[t] + (1 - alpha) * ema[t - 1]
    return ema