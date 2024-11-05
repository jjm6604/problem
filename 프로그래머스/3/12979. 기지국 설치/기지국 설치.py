def solution(n, stations, w):
    answer = 0
    lst = []
    k = 1
    
    for s in stations:
        if k <= s - w - 1:
            lst.append([k, s - w - 1])
        k = s + w + 1
    
    if k <= n:
        lst.append([k, n])

    for start, end in lst:
        answer += (end - start + 1) // (2 * w + 1)
        if (end - start + 1) % (2 * w + 1):
            answer += 1
            
    return answer