import sys
from collections import deque
d = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
T = int(sys.stdin.readline())
for t in range(T):
    l = int(input())
    x1, y1 = map(int, sys.stdin.readline().split())
    x2, y2 = map(int, sys.stdin.readline().split())
    v = set()
    q = deque()
    q.append([x1, y1])
    v = [[0] * l for _ in range(l)]
    v[x1][y1] = 1
    result = 0
    while q and not result:
        x, y = q.popleft()
        for i in range(8):
            nx = x + d[i][0]
            ny = y + d[i][1]
            if 0 <= nx < l and 0 <= ny < l and v[nx][ny] == 0:
                q.append([nx, ny])
                v[nx][ny] = v[x][y] + 1
                if nx == x2 and ny == y2:
                    result = v[nx][ny]
    if result:
        result -= 1
    print(result)
