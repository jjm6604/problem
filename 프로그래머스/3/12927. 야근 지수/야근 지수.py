def solution(n, works):
    answer = 0
    works.sort(reverse=True)
    k = 0
    l = 0
    N = len(works)
    works.append(0)
    if sum(works) <= n:
        return 0
    while n > 0:
        if works[k+1] == works[0]:
                while k+1 < N and works[k+1] == works[0]:
                    k += 1
        if n - k - 1 >= 0:
            works[0] -= 1
            n -= k + 1 
            
                    
        else:
            break
    for i in range(1, k+1):
        works[i] = works[0]
    works.sort(reverse=True)
    for i in range(n):
        works[i] -= 1
    for work in works:
        answer += work ** 2
        
    
    return answer