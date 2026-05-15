import numpy as np

def matrix_inverse(A):
    """
    Compute the inverse of a square, non-singular matrix.

    Args:
        A: 2D NumPy array of shape (n, n)

    Returns:
        Inverse matrix as NumPy array,
        or None if matrix is invalid or singular.
    """

    # Convert input to NumPy array
    A = np.array(A, dtype=float)

    # Check if matrix is 2D and square
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        return None

    # Check if matrix is singular
    det = np.linalg.det(A)
    if np.isclose(det, 0):
        return None

    # Compute inverse
    return np.linalg.inv(A)
