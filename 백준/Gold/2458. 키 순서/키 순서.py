from collections import deque

def bfs(n):
    q = deque()
    q.append((n, 0))
    q.append((n, 1))
    v[n] = 1
    while q:
        x, direct = q.popleft()
        for l in lst[x][direct]:
            if v[l] == 0:
                v[l] = 1
                q.append((l, direct))
    if v.count(1) == N:
        return True
    return False


N, M = map(int, input().split())

lst = [[[] for _ in range(2)] for _ in range(N+1)]
res = 0
for i in range(M):
    a, b = map(int, input().split())
    lst[a][1].append(b)
    lst[b][0].append(a)

for i in range(1, N+1):
    v = [0] * (N+1)
    if bfs(i):
        res += 1
        
print(res)