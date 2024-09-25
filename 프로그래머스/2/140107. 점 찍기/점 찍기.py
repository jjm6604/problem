def solution(k, d):
    answer = 0
    x = 0
    n = d
    for i in range(0, d+1, k):
        value = (d ** 2 - i ** 2) ** 0.5
        answer += value // k + 1
        
    return answer