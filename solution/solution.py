def solution(S):
    """Get max distance between two identical digrams in S."""
    
    last_seen = {}
    max_distance = -1
    
    for i in range(len(S) - 1):
        digram = S[i:i+2]
            
        if digram in last_seen:
            distance = i - last_seen[digram]
            max_distance = max(max_distance, distance)
        else:
            last_seen[digram] = i
        
    return max_distance
