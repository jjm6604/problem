N, M, V = map(int, input().split())
lst = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    lst[a][b] = 1
    lst[b][a] = 1

s = []
v = [0] * (N+1)
n = V
v[n] = 1
result_dfs = [n]
while True:
    for i in range(N+1):
        if lst[n][i] == 1 and v[i] == 0:
            s.append(n)
            n = i
            v[n] = 1
            result_dfs.append(i)
            break
    else:
        if s:
            n = s.pop()
        else:
            break
q = []
v = [0] * (N+1)
v[V] = 1
q.append(V)
result_bfs = [V]
while q:
    n = q.pop(0)
    for i in range(N+1):
        if lst[n][i] == 1 and v[i] == 0:
            q.append(i)
            v[i] = 1
            result_bfs.append(i)
print(*result_dfs)
print(*result_bfs)