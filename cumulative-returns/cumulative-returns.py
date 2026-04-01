from typing import List

def cumulative_returns(returns: List[float]) -> List[float]:
    wealth = 1.0
    result = []
    
    for r in returns:
        wealth *= (1 + r)         
        result.append(wealth - 1)  
    
    return result