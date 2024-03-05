from collections import deque

direct = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N, M = map(int, input().split())
R, C, D = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
q = deque()
q.append((R, C, D))
v = [[0] * M for _ in range(N)]
v[R][C] = 1
cnt = 1
while q:
    x, y, way = q.popleft()
    for i in range(4):
        n = (way + 3 - i) % 4
        dx, dy = x + direct[n][0], y + direct[n][1]
        if 0 <= dx < N and 0 <= dy < M and MAP[dx][dy] == 0 and v[dx][dy] == 0:
            v[dx][dy] = 1
            cnt += 1
            q.append((dx, dy, n))
            break
    else:
        dx, dy = x-direct[way][0], y-direct[way][1]
        if MAP[dx][dy] == 0:
            q.append((dx, dy, way))
        elif MAP[dx][dy] == 1:
            break
print(cnt)