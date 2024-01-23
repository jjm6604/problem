from collections import deque

direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]

N, M = map(int, input().split())

MAP = [input() for _ in range(M)]

checked = [[0] * N for _ in range(M)]
blue_power = 0
white_power = 0

q = deque()
for i in range(M):
    for j in range(N):
        if checked[i][j] == 0:
            color = MAP[i][j]
            q.append((i, j))
            checked[i][j] = 1
            cnt = 1
            while q:
                x, y = q.popleft()
                for k in range(4):
                    dx, dy = x + direct[k][0], y + direct[k][1]
                    if 0 <= dx < M and 0 <= dy < N and checked[dx][dy] == 0 and MAP[dx][dy] == color:
                        checked[dx][dy] = 1
                        q.append((dx, dy))
                        cnt += 1
            if color == 'B':
                blue_power += cnt ** 2
            else:
                white_power += cnt ** 2
print(white_power, blue_power)
