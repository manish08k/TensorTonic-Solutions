def cyclic_encoding(values, period):
    """
    Encode cyclic features as sin/cos pairs.
    """
    if period <= 0:
        raise ValueError("period must be > 0")

    encoded = []
    
    for v in values:
        theta = 2 * math.pi * v / period
        sin_val = math.sin(theta)
        cos_val = math.cos(theta)
        encoded.append([sin_val, cos_val])
    
    return encoded