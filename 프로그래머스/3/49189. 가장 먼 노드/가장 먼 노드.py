from collections import deque

def solution(n, edge):
    answer = 0
    lst = [[] for _ in range(n+1)]
    for e in edge:
        lst[e[0]].append(e[1])
        lst[e[1]].append(e[0])
    q = deque()
    q.append((1, 1))
    value = 1
    v = [0] * (n+1)
    v[1] = 1
    
    while q:
        x, cnt = q.popleft()
        if value < cnt:
            answer = 1
            value = cnt
        else:
            answer += 1
        for l in lst[x]:
            if v[l] == 0:
                v[l] = cnt
                q.append((l, cnt + 1))
    
    return answer