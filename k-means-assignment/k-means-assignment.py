def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    
    Args:
        points: List of points (list of lists), e.g., [[x1, y1], [x2, y2], ...]
        centroids: List of centroid points
        
    Returns:
        assignments: List where index = point index, value = centroid index
    """
    assignments = []
    
    for p in points:
        min_dist = float('inf')
        closest_centroid = -1
        
        for i, c in enumerate(centroids):
            # Euclidean distance
            dist = sum((p[j] - c[j]) ** 2 for j in range(len(p))) ** 0.5
            
            if dist < min_dist:
                min_dist = dist
                closest_centroid = i
        
        assignments.append(closest_centroid)
    
    return assignments