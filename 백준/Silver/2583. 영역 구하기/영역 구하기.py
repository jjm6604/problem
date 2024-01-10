direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]
M, N, K = map(int, input().split())

MAP = [[0] * M for _ in range(N)]
v = [[0] * M for _ in range(N)]
lst = []
res = 0
for k in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            MAP[i][j] = 1
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 0 and v[i][j] == 0:
            cnt = 1
            res += 1
            x, y = i, j
            s = []
            v[i][j] = 1
            while True:
                for k in range(4):
                    dx = x + direct[k][0]
                    dy = y + direct[k][1]
                    if 0 <= dx < N and 0 <= dy < M and v[dx][dy] == 0 and MAP[dx][dy] == 0:
                        v[dx][dy] = 1
                        s.append((dx, dy))
                        cnt += 1
                if s:
                    x, y = s.pop()
                else:
                    break
            lst.append(cnt)
lst.sort()
print(res)
print(*lst)