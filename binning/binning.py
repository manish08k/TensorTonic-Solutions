def binning(values, num_bins):
    mn, mx = min(values), max(values)
    if mn == mx:
        return [0]*len(values)
    
    w = (mx - mn) / num_bins
    return [min(int((x - mn)/w), num_bins-1) for x in values]
