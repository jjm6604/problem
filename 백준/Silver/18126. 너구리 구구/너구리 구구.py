from collections import deque

N = int(input())
lst = [[] for _ in range(N)]
v = [0] * N
for _ in range(N-1):
    A, B, C = map(int, input().split())
    lst[A-1].append((B-1, C))
    lst[B-1].append((A-1, C))
q = deque()
q.append(0)
while q:
    x = q.popleft()
    for l in lst[x]:
        if v[l[0]] == 0:
            v[l[0]] = v[x] + l[1]
            q.append(l[0])
print(max(v))
