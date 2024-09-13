def solution(n):
    answer = 0
    lst = [0] * (n + 1)
    lst[0] = 1
    lst[2] = 3
    
    for i in range(4, n + 1, 2):
        lst[i] = (sum(lst) * 2 + lst[i-2]) % 1000000007

    answer = lst[-1] 
    return answer