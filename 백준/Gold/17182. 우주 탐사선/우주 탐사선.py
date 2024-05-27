def backtrack(x, n, time):
    global max_time
    if time >= max_time:
        return
    if n == N:
        max_time = time
        return
    for i in range(N):
        if x == i:
            continue
        if v[i] == 0:
            v[i] = 1
            backtrack(i, n+1, time + MAP[x][i])
            v[i] = 0

N, K = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if i == j or i == k or k == j:
                continue
            MAP[i][j] = min(MAP[i][j], MAP[i][k] + MAP[k][j])

v = [0] * N
v[K] = 1
max_time = float('inf')
backtrack(K, 1, 0)
print(max_time)