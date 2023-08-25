import sys
from collections import deque

M, N = map(int, sys.stdin.readline().strip().split())
lst = [list(map(int, sys.stdin.readline().strip())) for _ in range(M)]
direct = [(0, 1), (1, 0), (-1, 0), (0, -1)]

result = 'NO'
for i in range(N):
    if lst[0][i] == 0:
        sy = i
        v = set()
        q = deque()
        q.append([0, sy])
        v.add((0, sy))

        while q:
            x, y = q.popleft()
            if x == M-1:
                result = 'YES'
                print(result)
                exit(0)
            for i in range(4):
                dx = x + direct[i][0]
                dy = y + direct[i][1]
                if 0 <= dx < M and 0 <= dy < N and lst[dx][dy] == 0 and (dx, dy) not in v:
                    q.append([dx, dy])
                    v.add((dx,dy))
print(result)