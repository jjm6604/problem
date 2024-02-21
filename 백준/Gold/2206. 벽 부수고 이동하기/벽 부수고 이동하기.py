import sys
from collections import deque

direct = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def bfs():
    q = deque()
    q.append((0, 0, 1, True))
    v1 = [[0] * M for _ in range(N)]
    v2 = [[0] * M for _ in range(N)]
    v1[0][0] = 1
    while q:
        x, y, dist, flag = q.popleft()
        if x == N-1 and y == M-1:
            return dist
        for i in range(4):
            dx, dy = x + direct[i][0], y + direct[i][1]
            if flag:
                if 0 <= dx < N and 0 <= dy < M and v1[dx][dy] == 0 and MAP[dx][dy] == 0:
                    v1[dx][dy] = 1
                    q.append((dx, dy, dist + 1, flag))
                elif 0 <= dx < N and 0 <= dy < M and MAP[dx][dy] == 1 and flag:
                    v1[dx][dy] = 1
                    q.append((dx, dy, dist + 1, False))
            else:
                if 0 <= dx < N and 0 <= dy < M and v1[dx][dy] == 0 and v2[dx][dy] == 0 and MAP[dx][dy] == 0:
                    v2[dx][dy] = 1
                    q.append((dx, dy, dist + 1, flag))

    return -1


N, M = map(int, input().split())

MAP = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

lst = []
res = [float('inf')]
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 1:
            lst.append((i, j))
print(bfs())
