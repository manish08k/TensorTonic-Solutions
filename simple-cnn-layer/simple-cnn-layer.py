import numpy as np

def conv2d(x, W, b):
    N, C_in, H, W_in = x.shape
    C_out, _, KH, KW = W.shape

    H_out = H - KH + 1
    W_out = W_in - KW + 1

    y = np.zeros((N, C_out, H_out, W_out), dtype=float)

    for i in range(H_out):
        for j in range(W_out):
            patch = x[:, :, i:i+KH, j:j+KW]

            y[:, :, i, j] = np.tensordot(
                patch, W, axes=([1, 2, 3], [1, 2, 3])
            ) + b

    return y