import numpy as np

def rnn_step_backward(dh, cache):
    """
    Backward pass for a single vanilla RNN step.

    Args:
        dh: Upstream gradient, shape (H,)
        cache: [x_t, h_prev, h_t, W, U, b]

    Returns:
        Tuple:
        (dx_t, dh_prev, dW, dU, db)
    """

    # Unpack cache
    x_t, h_prev, h_t, W, U, b = cache

    # Convert to NumPy arrays
    dh = np.asarray(dh)
    x_t = np.asarray(x_t)
    h_prev = np.asarray(h_prev)
    h_t = np.asarray(h_t)
    W = np.asarray(W)
    U = np.asarray(U)

    # Gradient through tanh
    dz = dh * (1 - h_t ** 2)

    # Gradients
    dx_t = W.T @ dz
    dh_prev = U.T @ dz

    dW = np.outer(dz, x_t)
    dU = np.outer(dz, h_prev)

    db = dz.copy()

    return dx_t, dh_prev, dW, dU, db
