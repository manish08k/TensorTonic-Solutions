import numpy as np

def expected_value_discrete(x, p):
    x=np.array(x)
    p=np.array(p)
    if not np.isclose(np.sum(p), 1):
        raise ValueError("Invalid probabilities")
    a=sum(x*p)
    return a