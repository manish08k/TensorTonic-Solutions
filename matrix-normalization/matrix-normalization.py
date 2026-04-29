import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    try:
        # Convert input
        x = np.asarray(matrix, dtype=np.float32)

        # Validate 2D
        if x.ndim != 2:
            return None

        # Validate axis
        if axis not in (0, 1, None):
            return None

        # Compute norm
        if norm_type == 'l1':
            norm = np.sum(np.abs(x), axis=axis, keepdims=True)
        elif norm_type == 'l2':
            norm = np.sqrt(np.sum(x ** 2, axis=axis, keepdims=True))
        elif norm_type == 'max':
            norm = np.max(np.abs(x), axis=axis, keepdims=True)
        else:
            return None

        # Avoid division by zero
        norm = np.where(norm == 0, 1, norm)

        # Normalize
        normalized = x / norm

        return normalized

    except:
        return None