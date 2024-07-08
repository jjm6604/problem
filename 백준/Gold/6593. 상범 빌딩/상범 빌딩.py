from collections import deque

direct = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

while True:
    x, y, z = map(int, input().split())
    if x == 0 and y == 0 and z == 0:
        break
    MAP = []
    v = [[[-1] * z for _ in range(y)] for _ in range(x)]
    result = 'Trapped!'
    for i in range(x):
        lst = [input() for _ in range(y)]
        MAP.append(lst)
        input()
    for i in range(x):
        for j in range(y):
            for k in range(z):
                if MAP[i][j][k] == 'S':
                    S = [i, j, k]
                    v[i][j][k] = 0
                elif MAP[i][j][k] == 'E':
                    E = [i, j, k]


    q = deque()
    q.append(S)
    while q:
        nx, ny, nz = q.popleft()
        for d in direct:
            dx, dy, dz = nx + d[0], ny + d[1], nz + d[2]
            if 0 <= dx < x and 0 <= dy < y and 0 <= dz < z and MAP[dx][dy][dz] != '#' and v[dx][dy][dz] == -1:
                if MAP[dx][dy][dz] == 'E':
                    result = f'Escaped in {v[nx][ny][nz] + 1} minute(s).'
                    break
                v[dx][dy][dz] = v[nx][ny][nz] + 1
                q.append([dx, dy, dz])
        else:
            continue
        break
    print(result)
