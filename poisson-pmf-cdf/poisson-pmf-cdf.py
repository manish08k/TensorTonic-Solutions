import numpy as np
from scipy.special import gammaln

def poisson_pmf_cdf(lam, k):
    # Ensure valid inputs
    if lam <= 0 or k < 0:
        raise ValueError("lam must be > 0 and k >= 0")

    # Convert to int
    k = int(k)

    # ---- PMF ----
    log_pmf = -lam + k * np.log(lam) - gammaln(k + 1)
    pmf = np.exp(log_pmf)

    # ---- CDF ----
    i = np.arange(0, k + 1)
    log_terms = -lam + i * np.log(lam) - gammaln(i + 1)
    cdf = np.sum(np.exp(log_terms))

    return float(pmf), float(cdf)