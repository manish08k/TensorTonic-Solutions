def binomial_pmf_cdf(n, p, k):
    if p == 0:
        return (1.0 if k == 0 else 0.0, 1.0)
    if p == 1:
        return (1.0 if k == n else 0.0, 1.0 if k == n else 0.0)

    prob = (1 - p) ** n   # P(X=0)
    cdf = prob

    for i in range(1, k + 1):
        prob *= (n - i + 1) / i * (p / (1 - p))
        cdf += prob

    return prob, cdf