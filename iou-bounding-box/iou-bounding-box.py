def iou(a, b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    # Intersection coordinates
    x_left = max(a[0], b[0])
    y_top = max(a[1], b[1])
    x_right = min(a[2], b[2])
    y_bottom = min(a[3], b[3])

    # No overlap
    if x_right <= x_left or y_bottom <= y_top:
        return 0.0

    # Areas
    intersection = (x_right - x_left) * (y_bottom - y_top)

    area_a = (a[2] - a[0]) * (a[3] - a[1])
    area_b = (b[2] - b[0]) * (b[3] - b[1])

    union = area_a + area_b - intersection

    # Avoid division by zero
    if union == 0:
        return 0.0

    return intersection / union