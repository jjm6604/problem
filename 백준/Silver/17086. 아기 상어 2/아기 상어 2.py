import sys
from collections import deque
direct = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def bfs(x, y):
    q = deque()
    v = [[0] * M for _ in range(N)]
    q.append([x, y])
    v[x][y] = 1
    while q:
        qx, qy = q.popleft()
        for k in range(8):
            ni = qx + direct[k][0]
            nj = qy + direct[k][1]
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0 and lst[ni][nj] == 0:
                q.append([ni, nj])
                v[ni][nj] = v[qx][qy] + 1
            elif 0 <= ni < N and 0 <= nj < M and lst[ni][nj] == 1:
                return v[qx][qy]

N, M = map(int, sys.stdin.readline().strip().split())
lst = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
result = []
for i in range(N):
    for j in range(M):
        if lst[i][j] == 0:
            result.append(bfs(i, j))
print(max(result))