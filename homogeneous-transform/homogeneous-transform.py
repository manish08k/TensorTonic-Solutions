import numpy as np

def apply_homogeneous_transform(T, points):
    T = np.asarray(T)
    points = np.asarray(points)

    single = False
    if points.ndim == 1:
        points = points.reshape(1, 3)
        single = True

    ones = np.ones((points.shape[0], 1))
    points_h = np.hstack([points, ones])

    transformed = points_h @ T.T

    result = transformed[:, :3]

    if single:
        return result[0]
    return result