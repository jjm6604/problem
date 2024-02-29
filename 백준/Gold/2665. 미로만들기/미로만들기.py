from collections import deque

direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]
N = int(input())
MAP = [list(map(int, input())) for _ in range(N)]
v = [[float('inf')] * N for _ in range(N)]
q = deque()
q.append((0, 0, 0))
v[0][0] = 0
while q:
    x, y, cnt = q.popleft()
    for d in direct:
        dx, dy = x + d[0], y + d[1]
        if 0 <= dx < N and 0 <= dy < N:
            if MAP[dx][dy] == 0:
                if v[dx][dy] > cnt + 1:
                    v[dx][dy] = cnt + 1
                    q.append((dx, dy, cnt + 1))
            else:
                if v[dx][dy] > cnt:
                    v[dx][dy] = cnt
                    q.append((dx, dy, cnt))
print(v[N-1][N-1])