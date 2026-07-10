def autocorrelation(series, max_lag):
    """
    Compute the autocorrelation of a time series for lags 0 to max_lag.
    """
    n = len(series)
    mean = sum(series) / n

    # Total variance (gamma_0)
    variance = sum((x - mean) ** 2 for x in series)

    # Handle constant series
    if variance == 0:
        return [1.0] + [0.0] * max_lag

    result = []

    for lag in range(max_lag + 1):
        covariance = 0.0
        for i in range(n - lag):
            covariance += (series[i] - mean) * (series[i + lag] - mean)

        result.append(covariance / variance)

    return result