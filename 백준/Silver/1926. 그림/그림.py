N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
v = [[0] * M for _ in range(N)]

direct = [(0, 1), (0, -1), (-1, 0), (1, 0)]
cnt = 0
max_value = 0
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 1 and v[i][j] == 0:
            cnt += 1
            q = [(i, j)]
            v[i][j] = 1
            value = 1
            while q:
                x, y = q.pop(0)
                for k in range(4):
                    dx = x + direct[k][0]
                    dy = y + direct[k][1]
                    if 0 <= dx < N and 0 <= dy < M and MAP[dx][dy] == 1 and v[dx][dy] == 0:
                        v[dx][dy] = 1
                        value += 1
                        q.append((dx, dy))
            if max_value < value:
                max_value = value

print(cnt)
print(max_value)