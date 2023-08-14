di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
result = []

M, N, K = map(int, input().split())
lst = [[0] * M for _ in range(N)]
for k in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            lst[i][j] = 1
v = [[0] * M for _ in range(N)]
coord = []
for i in range(N):
    for j in range(M):
        if lst[i][j] == 0 and v[i][j] == 0:
            cnt = 1
            x, y = i, j
            v[i][j] = 1
            while True:
                for k in range(4):
                    dx = x + di[k]
                    dy = y + dj[k]
                    if 0 <= dx < N and 0 <= dy < M and lst[dx][dy] == 0 and v[dx][dy] == 0:
                        cnt += 1
                        v[dx][dy] = 1
                        coord.append([dx, dy])
                else:
                    if coord:
                        x, y = coord.pop()
                    else:
                        break
            result.append(cnt)
result.sort()
print(len(result))
print(*result)