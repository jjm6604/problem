def solution(gems):
    answer = []
    gem_dict = {}
    
    for gem in gems:
        gem_dict[gem] = 0
    
    N = len(gems)
    M = len(gem_dict)
    
    value = 0
    
    for i in range(M):
        gem_dict[gems[i]] += 1
        if gem_dict[gems[i]] == 1:
            value += 1
    
    start, end = 0, M - 1
    min_length = N
    
    while end >= start:
        if value == M:
            if min_length > end - start:
                min_length = end - start
                answer = [start + 1, end + 1]
            gem_dict[gems[start]] -= 1
            if gem_dict[gems[start]] == 0:
                value -= 1
            start += 1
        else:
            if end == N - 1:
                break
            end += 1
            gem_dict[gems[end]] += 1
            if gem_dict[gems[end]] == 1:
                value += 1
        
    
    return answer