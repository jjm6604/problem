from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    MAP = [[] for _ in range(n + 1)]
    v = [-1] * (n + 1)
    
    for x, y in roads:
        MAP[x].append(y)
        MAP[y].append(x)
    
    q = deque()
    q.append(destination)
    v[destination] = 0
    
    while q:
        location = q.popleft()
        for l in MAP[location]:
            if v[l] == -1:
                v[l] = v[location] + 1
                q.append(l)
    
    for source in sources:
        answer.append(v[source])
    
    return answer