import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().strip().split())
lst = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    lst[a].append(b)

# for l in lst:
#     l.sort()

q = deque()
v = [0] * (N+1)
q.append(X)
v[X] = 1
flag = True
result = []
while q and flag:
    x = q.popleft()
    for l in lst[x]:
        if v[l] == 0:
            q.append(l)
            v[l] = v[x] + 1
            if v[l] == K+1:
                result.append(l)

if result:
    result.sort()
    for r in result:
        print(r)
else:
    print(-1)