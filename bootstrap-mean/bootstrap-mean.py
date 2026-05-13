import numpy as np

def bootstrap_mean(x, n_bootstrap=1000, ci=0.95, rng=None):
    """
    Returns: (boot_means, lower, upper)
    """
    x = np.asarray(x, dtype=float)
    n = len(x)

    # Use provided RNG or fallback
    if rng is None:
        rng = np.random.default_rng()

    # Generate bootstrap sample indices
    indices = rng.integers(0, n, size=(n_bootstrap, n))

    # Bootstrap samples
    samples = x[indices]

    # Mean of each bootstrap sample
    boot_means = samples.mean(axis=1)

    # Confidence interval bounds
    alpha = 1.0 - ci
    lower = np.quantile(boot_means, alpha / 2)
    upper = np.quantile(boot_means, 1 - alpha / 2)

    return boot_means, float(lower), float(upper)