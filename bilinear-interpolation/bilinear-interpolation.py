import math

def bilinear_resize(image, new_h, new_w):
    """
    Resize a 2D grid using bilinear interpolation.
    """

    H = len(image)
    W = len(image[0])

    output = []

    for i in range(new_h):

        row = []

        # Map output y to source y
        if new_h == 1:
            src_y = 0
        else:
            src_y = i * (H - 1) / (new_h - 1)

        y0 = int(math.floor(src_y))
        y1 = min(y0 + 1, H - 1)

        dy = src_y - y0

        for j in range(new_w):

            # Map output x to source x
            if new_w == 1:
                src_x = 0
            else:
                src_x = j * (W - 1) / (new_w - 1)

            x0 = int(math.floor(src_x))
            x1 = min(x0 + 1, W - 1)

            dx = src_x - x0

            # Four neighboring pixels
            top_left = image[y0][x0]
            bottom_left = image[y1][x0]
            top_right = image[y0][x1]
            bottom_right = image[y1][x1]

            # Bilinear interpolation
            value = (
                top_left * (1 - dy) * (1 - dx) +
                bottom_left * dy * (1 - dx) +
                top_right * (1 - dy) * dx +
                bottom_right * dy * dx
            )

            row.append(value)

        output.append(row)

    return output