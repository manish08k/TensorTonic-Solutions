import numpy as np

def calculate_eigenvalues(matrix):
    try:
        A = np.array(matrix)

        if A.size == 0:
            return None

        if A.ndim != 2 or A.shape[0] != A.shape[1]:
            return None

        eigenvalues = np.linalg.eigvals(A)

        eigenvalues = np.array(eigenvalues, dtype=complex)

        eigenvalues = sorted(eigenvalues, key=lambda x: (x.real, x.imag))

        return np.array(eigenvalues)

    except Exception:
        return None