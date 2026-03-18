import numpy as np

def dot_product(x, y):
    if len(x) != len(y):
        raise ValueError("Vectors must be of same length")
    
    return sum(i * j for i, j in zip(x, y))