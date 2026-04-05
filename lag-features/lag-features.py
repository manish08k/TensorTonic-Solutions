def lag_features(series, lags):
    """
    Create a lag feature matrix from the time series.
    """
    result = []
    max_lag = max(lags)

    for t in range(max_lag, len(series)):
        row = []
        for lag in lags:
            row.append(series[t - lag])
        result.append(row)

    return result