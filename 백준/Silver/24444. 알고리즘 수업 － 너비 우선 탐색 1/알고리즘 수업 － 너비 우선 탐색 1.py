import sys
from collections import deque
n, m, r = map(int, sys.stdin.readline().strip().split())
lst = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    lst[a].append(b)
    lst[b].append(a)
q = deque()
v = [0] * (n+1)
q.append(r)
v[r] = 1
result = [0] * n
k = 0
for i in range(n+1):
    lst[i].sort()

while q:
    k += 1
    x = q.popleft()
    result[x-1] = k
    for l in lst[x]:
        if v[l] == 0:
            q.append(l)
            v[l] = 1
for r in result:
    print(r)