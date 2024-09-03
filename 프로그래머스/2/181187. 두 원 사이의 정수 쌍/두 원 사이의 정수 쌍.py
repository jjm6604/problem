def solution(r1, r2):
    answer = 0
    k = r2
    for i in range(1, r2 + 1):
        for j in range(k, 0, -1):
            if ((i ** 2 + j ** 2) ** 0.5) <= r2:
                k = j
                answer += k
                break
    
    k = r1
    for i in range(1, r1 + 1):
        for j in range(k, 0, -1):
            if ((i ** 2 + j ** 2) ** 0.5) < r1:
                k = j
                answer -= k
                break
                
    answer *= 4
    answer += (r2 - r1 + 1) * 4
    
    return answer