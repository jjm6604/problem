from collections import deque

def cut_wire(n, k, wires):
    lst = [[] for _ in range(n+1)]
    for i in range(n-1):
        if i == k:
            continue
        lst[wires[i][0]].append(wires[i][1])
        lst[wires[i][1]].append(wires[i][0])
    
    q = deque()
    cnt = 1
    q.append(1)
    v = [0] * (n + 1)
    v[1] = 1
    while q:
        x = q.popleft()
        for l in lst[x]:
            if v[l] == 0:
                cnt += 1
                v[l] = 1
                q.append(l)
    value = abs(n - (2 * cnt))

    return value

def solution(n, wires):
    

    res = set()
    for i in range(n-1):
        res.add(cut_wire(n, i, wires))
    
    answer = min(res)
    
    return answer