from collections import deque

direct = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
N = int(input())
x1, y1, x2, y2 = map(int, input().split())
v = [[0] * N for _ in range(N)]
q = deque()
q.append((x1, y1, 0))
v[x1][y1] = 1
result = -1
while q:
    x, y, cnt = q.popleft()
    if x == x2 and y == y2:
        result = cnt
        break
    for d in direct:
        dx, dy = x + d[0], y + d[1]
        if 0 <= dx < N and 0 <= dy < N and v[dx][dy] == 0:
            q.append((dx, dy, cnt + 1))
            v[dx][dy] = 1
print(result)