from collections import deque

direct = [(0, 1), (1, 0)]
N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
start = (0, 0)
q = deque()
q.append(start)
res = 'Hing'
v = [[0] * N for _ in range(N)]
while q:
    x, y = q.popleft()
    if MAP[x][y] == -1:
        res = 'HaruHaru'
        break
    for i in range(2):
        dx, dy = x + direct[i][0] * MAP[x][y], y + direct[i][1] * MAP[x][y]

        if 0 <= dx < N and 0 <= dy < N and v[dx][dy] == 0:
            q.append((dx, dy))
            v[dx][dy] = 1

print(res)