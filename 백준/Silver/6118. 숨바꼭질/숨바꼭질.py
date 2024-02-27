from collections import deque

N, M = map(int, input().split())
lst = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
v = [0] * (N+1)
q = deque()
q.append((1, 0))
v[1] = 1
res = [1]
value = 0
while q:
    x, cnt = q.popleft()
    if value < cnt:
        res = [x]
        value = cnt
    else:
        res.append(x)
    for l in lst[x]:
        # for i in l:
        if v[l] == 0:
            v[l] = 1
            q.append((l, cnt+1))

print(min(res), value, len(res))