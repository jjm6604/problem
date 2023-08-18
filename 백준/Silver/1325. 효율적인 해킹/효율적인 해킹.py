import sys
from collections import deque

def bfs(start):
    q = deque()
    v = [0] * (N+1)
    q.append(start)
    v[start] = 1
    cnt = 1
    while q:
        x = q.popleft()
        for i in lst[x]:
            if not v[i]:
                q.append(i)
                v[i] = 1
                cnt += 1
    return [start, cnt]


N, M = map(int, sys.stdin.readline().split())
lst = [[] for _ in range(N+1)]
input_data = []
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    input_data.append((a, b))

for a, b in input_data:
    lst[b].append(a)

result = []
MAX = 0
for i in range(1, N+1):
    idx, num = bfs(i)
    if MAX == num:
        result.append(idx)
    elif MAX < num:
        MAX = num
        result = [idx]
print(*result)