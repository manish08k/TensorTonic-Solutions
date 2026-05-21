import numpy as np

def rotate_around_z(points, theta):
    points = np.asarray(points, dtype=float)

    cos_t = np.cos(theta)
    sin_t = np.sin(theta)

    R = np.array([
        [cos_t, -sin_t, 0],
        [sin_t,  cos_t, 0],
        [0,      0,     1]
    ])

    # Single point
    if points.ndim == 1:
        return R @ points

    # Multiple points
    return points @ R.T