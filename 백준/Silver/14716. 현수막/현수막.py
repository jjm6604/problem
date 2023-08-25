import sys
from collections import deque
M, N = map(int, sys.stdin.readline().strip().split())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
q = deque()
v = set()
cnt = 0
for i in range(M):
    for j in range(N):
        if lst[i][j] == 1 and (i, j) not in v:
            cnt += 1
            q.append([i, j])
            v.add((i, j))
            while q:
                x, y = q.popleft()
                for k in range(8):
                    nx = x + d[k][0]
                    ny = y + d[k][1]
                    if 0 <= nx < M and 0 <= ny < N and lst[nx][ny] == 1 and (nx, ny) not in v:
                        q.append([nx, ny])
                        v.add((nx, ny))
print(cnt)