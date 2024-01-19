from collections import deque

direct = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def bfs(x, y):
    visited[x][y] = 1
    q = deque()
    q.append((x, y))
    cnt1, cnt2 = 0, 0
    flag = True
    while q:
        nx, ny = q.popleft()
        if MAP[nx][ny] == 'o':
            cnt1 += 1
        elif MAP[nx][ny] == 'v':
            cnt2 += 1
        for i in range(4):
            dx, dy = nx + direct[i][0], ny + direct[i][1]
            if (dx in [0, N-1] or dy in [0, M-1]) and 0 <= dx < N and 0 <= dy < M and visited[dx][dy] == 0 and MAP[dx][dy] == '.':
                flag = False
                visited[dx][dy] = 1
                q.append((dx, dy))
            if 1 <= dx < N-1 and 1 <= dy < M-1 and visited[dx][dy] == 0 and MAP[dx][dy] != '#':
                visited[dx][dy] = 1
                q.append((dx, dy))

    if flag:
        return (cnt1, cnt2)
    else:
        return (0, 0)



N, M = map(int, input().split())
visited = [[0] * M for _ in range(N)]
MAP = [input() for _ in range(N)]
result = [0, 0]

for i in range(1, N-1):
    for j in range(1, M-1):
        if visited[i][j] == 0 and MAP[i][j] != '#':
            a, b = bfs(i, j)

            if a > b:
                result[0] += a
            else:
                result[1] += b
print(*result)
