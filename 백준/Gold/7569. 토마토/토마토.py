from collections import deque

direct = [(0, 0, 1), (0, 0, -1), (0, -1, 0), (0, 1, 0), (1, 0, 0), (-1, 0, 0)]

def bfs(coord):
    q = deque(coord)

    while q:
        x, y, z = q.popleft()
        for i in range(6):
            dx, dy, dz = x + direct[i][0], y + direct[i][1], z + direct[i][2]
            if 0 <= dx < H and 0 <= dy < N and 0 <= dz < M and days[dx][dy][dz] == -1:
                days[dx][dy][dz] = days[x][y][z] + 1
                q.append((dx, dy, dz))

    day = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if days[i][j][k] == -1:
                    return -1
                if day < days[i][j][k]:
                    day = days[i][j][k]
    return day


M, N, H = map(int, input().split())
boxes = [[list(map(int, input().split())) for _ in range(N)] for _ in range (H)]

days = [[[-1] * M for _ in range(N)] for _ in range(H)]
lst = []
for i in range(H):
    for j in range(N):
        for k in range(M):
            if boxes[i][j][k] == 1:
                lst.append((i, j, k))
                days[i][j][k] = 0
            if boxes[i][j][k] == -1:
                days[i][j][k] = 0

result = bfs(lst)
print(result)