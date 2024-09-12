def solution(n):
    answer = 0
    lst = [0] * n
    lst[0] = 1
    lst[1] = 2
    
    for i in range(2, n):
        lst[i] = (lst[i-2] + lst[i-1]) % 1000000007
        
    answer = lst[-1]
    
    return answer