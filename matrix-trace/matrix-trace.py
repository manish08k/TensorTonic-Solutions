import numpy as np

def matrix_trace(A):
    n = len(A)
    trace = 0
    
    for i in range(n):
        trace += A[i][i]
    
    return trace