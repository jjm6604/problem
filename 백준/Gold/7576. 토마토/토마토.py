from collections import deque

direct = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def bfs(coord):
    q = deque(coord)
    while q:
        x, y = q.popleft()
        for i in range(4):
            dx, dy = x + direct[i][0], y + direct[i][1]
            if 0 <= dx < N and 0 <= dy < M and days[dx][dy] == -1 and boxes[dx][dy] == 0:
                days[dx][dy] = days[x][y] + 1
                q.append((dx, dy))

    day = 0
    for i in range(N):
        for j in range(M):
            if days[i][j] == -1:
                return -1
            if day < days[i][j]:
                day = days[i][j]
    return day


M, N = map(int, input().split())
boxes = [list(map(int, input().split())) for _ in range(N)]
days = [[-1] * M for _ in range(N)]
lst = []
for i in range(N):
    for j in range(M):
        if boxes[i][j] == 1:
            lst.append((i, j))
            days[i][j] = 0
        if boxes[i][j] == -1:
            days[i][j] = 0

res = bfs(lst)
print(res)