def solution(n, s):
    if s < n:
        return [-1]
    
    x = s // n
    y = s % n
    
    answer = [x] * n
    
    for i in range(y):
        answer[-(i+1)] += 1
        
    return answer