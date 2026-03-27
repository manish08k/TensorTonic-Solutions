def deduplicate(records, key_columns, strategy):
    groups = {}
    order = []
    
    for idx, record in enumerate(records):
        key = tuple(record[col] for col in key_columns)
        
        if key not in groups:
            groups[key] = []
            order.append(key)
        
        groups[key].append((idx, record))
    
    result = []
    
    for key in order:
        group = groups[key]
        
        if strategy == "first":
            chosen = group[0][1]
        
        elif strategy == "last":
            chosen = group[-1][1]
        
        elif strategy == "most_complete":
            def none_count(rec):
                return sum(1 for v in rec.values() if v is None)
            
            best = group[0]
            min_none = none_count(best[1])
            
            for item in group:
                count = none_count(item[1])
                if count < min_none:
                    best = item
                    min_none = count
            
            chosen = best[1]
        
        result.append(chosen)
    
    return result