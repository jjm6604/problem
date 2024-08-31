def solution(n):
    answer = 0
    
    start, end = 1, 0
    value = 0
    while end <= n:
        
        if value < n:
            end += 1
            value += end
        else:
            value -= start
            start += 1
        if value == n:
            answer += 1
            
    return answer