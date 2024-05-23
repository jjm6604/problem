from collections import deque

N, M, T = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
q = deque()
v1 = [[0] * M for _ in range(N)]
v2 = [[0] * M for _ in range(N)]
v1[0][0] = 1
q.append((0, 0, 0, False))

while q:
    x, y, t, flag = q.popleft()
    if x == N-1 and y == M-1:
        print(t)
        break
    if t <= T:
        for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dx = x + d[0]
            dy = y + d[1]
            if 0 <= dx < N and 0 <= dy < M:
                if flag and v2[dx][dy] == 0:
                    q.append((dx, dy, t+1, flag))
                    v2[dx][dy] = 1
                elif v1[dx][dy] == 0:
                    if MAP[dx][dy] == 2:
                        v1[dx][dy] = 1
                        q.append((dx, dy, t+1, True))
                    elif MAP[dx][dy] == 0:
                        q.append((dx, dy, t+1, flag))
                        v1[dx][dy] = 1
else:
    print("Fail")