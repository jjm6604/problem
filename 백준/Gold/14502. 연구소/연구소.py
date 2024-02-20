from collections import deque
direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs():
    v = [[0] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 2:
                q = deque()
                q.append((i, j))
                while q:
                    x, y = q.popleft()
                    cnt += 1
                    if cnt >= min(res):
                        return
                    for d in direct:
                        dx, dy = x + d[0], y + d[1]
                        if 0 <= dx < N and 0 <= dy < M and v[dx][dy] == 0 and MAP[dx][dy] == 0:
                            v[dx][dy] = 1
                            q.append((dx, dy))

    res.add(cnt)
    return

def backtrack(n, m):
    if n == 3:
        bfs()
        return
    if m == len(blanks):
        return
    x, y = blanks[m]
    MAP[x][y] = 1
    backtrack(n+1, m+1)
    MAP[x][y] = 0
    backtrack(n, m+1)

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
res = set()
res.add(N*M)
blanks = []
wall = 3
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 0:
            blanks.append((i, j))
        if MAP[i][j] == 1:
            wall += 1
backtrack(0, 0)
result = N * M - min(res) - wall
print(result)