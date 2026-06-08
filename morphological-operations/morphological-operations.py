def morphological_op(image, kernel, operation):
    """
    Apply morphological erosion or dilation to a binary image.
    """
    rows = len(image)
    cols = len(image[0])

    k_rows = len(kernel)
    k_cols = len(kernel[0])

    pad_r = k_rows // 2
    pad_c = k_cols // 2

    # Zero-padded image
    padded = [[0] * (cols + 2 * pad_c) for _ in range(rows + 2 * pad_r)]

    for i in range(rows):
        for j in range(cols):
            padded[i + pad_r][j + pad_c] = image[i][j]

    result = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):

            if operation == "erode":
                value = 1
                for ki in range(k_rows):
                    for kj in range(k_cols):
                        if kernel[ki][kj] == 1:
                            if padded[i + ki][j + kj] != 1:
                                value = 0
                                break
                    if value == 0:
                        break
                result[i][j] = value

            else:  # dilate
                value = 0
                for ki in range(k_rows):
                    for kj in range(k_cols):
                        if kernel[ki][kj] == 1 and padded[i + ki][j + kj] == 1:
                            value = 1
                            break
                    if value == 1:
                        break
                result[i][j] = value

    return result