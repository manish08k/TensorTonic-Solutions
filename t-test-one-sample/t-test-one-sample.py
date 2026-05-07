import numpy as np

def t_test_one_sample(x, mu0):
    # Convert to NumPy array
    x = np.array(x, dtype=float)

    # Sample size
    n = len(x)

    # Sample mean
    mean = np.mean(x)

    # Sample standard deviation with Bessel correction
    s = np.std(x, ddof=1)

    # Compute t-statistic
    t_stat = (mean - mu0) / (s / np.sqrt(n))

    return float(t_stat)