def solution(x):
    answer = True
    n = 0
    k = x
    
    while k:
        n += k % 10
        k //= 10
    
    if x % n:
        answer = False
        
    return answer