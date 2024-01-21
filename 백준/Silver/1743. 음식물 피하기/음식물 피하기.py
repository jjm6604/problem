from collections import deque

direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    cnt = 1
    while q:
        nx, ny = q.popleft()
        for i in range(4):
            dx, dy = nx + direct[i][0], ny + direct[i][1]
            if 0 <= dx < N and 0 <= dy < M and visited[dx][dy] == 0 and MAP[dx][dy] == 1:
                visited[dx][dy] = 1
                cnt += 1
                q.append((dx, dy))
    return cnt

N, M, K = map(int, input().split())
MAP = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]
for _ in range(K):
    x, y = map(int, input().split())
    MAP[x-1][y-1] = 1

res = 0
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 1 and visited[i][j] == 0:
            value = bfs(i, j)
            if res < value:
                res = value

print(res)