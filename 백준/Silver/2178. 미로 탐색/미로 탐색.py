direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]
N, M = map(int, input().split())
MAP = [list(map(int, input())) for _ in range(N)]
q = []
q.append([0, 0])
v = [[0] * M for _ in range(N)]
v[0][0] = 1

while q:
    x, y = q.pop(0)
    for k in range(4):
        nx = x + direct[k][0]
        ny = y + direct[k][1]
        if 0 <= nx < N and 0 <= ny < M and v[nx][ny] == 0 and MAP[nx][ny] == 1:
            q.append([nx, ny])
            v[nx][ny] = v[x][y] + 1

print(v[N-1][M-1])
