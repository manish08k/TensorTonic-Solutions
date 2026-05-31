def nms(boxes, scores, iou_threshold):
    """
    Apply Non-Maximum Suppression.
    """
    if not boxes:
        return []

    # Sort indices by score (descending)
    order = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)

    kept = []

    while order:
        current = order.pop(0)
        kept.append(current)

        remaining = []

        for idx in order:
            # Current box
            x1A, y1A, x2A, y2A = boxes[current]

            # Candidate box
            x1B, y1B, x2B, y2B = boxes[idx]

            # Intersection
            ix1 = max(x1A, x1B)
            iy1 = max(y1A, y1B)
            ix2 = min(x2A, x2B)
            iy2 = min(y2A, y2B)

            inter_w = max(0, ix2 - ix1)
            inter_h = max(0, iy2 - iy1)
            inter_area = inter_w * inter_h

            # Areas
            areaA = (x2A - x1A) * (y2A - y1A)
            areaB = (x2B - x1B) * (y2B - y1B)

            # IoU
            union = areaA + areaB - inter_area
            iou = inter_area / union if union > 0 else 0

            # Keep only boxes with IoU below threshold
            if iou < iou_threshold:
                remaining.append(idx)

        order = remaining

    return kept