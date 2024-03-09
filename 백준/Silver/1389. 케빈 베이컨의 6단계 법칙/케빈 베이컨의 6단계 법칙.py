from collections import deque

N, M = map(int, input().split())
lst = [[] for _ in range(N+1)]

for i in range(M):
    A, B = map(int, input().split())
    lst[A].append(B)
    lst[B].append(A)

value = float('inf')
res = 0
for i in range(1, N+1):
    v = [-1] * (N+1)
    cnt = 0
    v[i] = 1
    q = deque()
    q.append(i)
    while q:
        x = q.popleft()
        for l in lst[x]:
            if v[l] == -1:
                v[l] = v[x] + 1
                q.append(l)
        if sum(v) + 1 >= value:
            break
        if v.count(-1) == 1:
            value = sum(v) + 1
            res = i
print(res)