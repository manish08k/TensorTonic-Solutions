def double_exponential_smoothing(series, alpha, beta):
    level = float(series[0])
    trend = float(series[1] - series[0])

    result = [level]

    for i in range(1, len(series)):
        prev_level = level

        level = alpha * series[i] + (1 - alpha) * (level + trend)
        trend = beta * (level - prev_level) + (1 - beta) * trend

        result.append(float(level))

    return result