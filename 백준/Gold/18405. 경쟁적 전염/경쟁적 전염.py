from collections import deque

direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]
N, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
v = [[-1] * N for _ in range(N)]
q = deque()
for i in range(N):
    for j in range(N):
        if MAP[i][j] != 0:
            # x, y, k, cnt
            q.append((i, j, MAP[i][j], 1))
            v[i][j] = 0
while q:
    x, y, k, cnt = q.popleft()
    if cnt > S:
        break
    for d in direct:
        dx, dy = x + d[0], y + d[1]
        if 0 <= dx < N and 0 <= dy < N and (MAP[dx][dy] == 0 or (v[dx][dy] == cnt and MAP[dx][dy] > k)):
            MAP[dx][dy] = k
            v[dx][dy] = cnt
            q.append((dx, dy, k, cnt+1))
print(MAP[X-1][Y-1])