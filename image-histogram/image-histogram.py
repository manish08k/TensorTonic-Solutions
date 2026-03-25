def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Initialize 256 bins (0–255)
    hist = [0] * 256
    
    # Count pixel frequencies
    for row in image:
        for pixel in row:
            hist[pixel] += 1
    
    return hist