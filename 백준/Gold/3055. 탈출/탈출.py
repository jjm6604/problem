from collections import deque

direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]

R, C = map(int, input().split())
MAP = [list(input()) for _ in range(R)]
v = [[0] * C for _ in range(R)]
res = 'KAKTUS'
q = deque()

for i in range(R):
    for j in range(C):
        if MAP[i][j] == 'D':
            end_point = (i, j)
        elif MAP[i][j] == 'S':
            start_point = (i, j)
            v[i][j] = 1
        elif MAP[i][j] == '*':
            q.append((i, j, 0, False))
q.append((*start_point, 0, True))

while q:
    x, y, time, flag = q.popleft()
    if flag and (x, y) == end_point:
        res = time
        break
    for d in direct:
        dx, dy = x + d[0], y + d[1]
        if flag and 0 <= dx < R and 0 <= dy < C and v[dx][dy] == 0 and (MAP[dx][dy] == '.' or MAP[dx][dy] == 'D'):
            q.append((dx, dy, time+1, flag))
            v[dx][dy] = 1
        elif not flag and 0 <= dx < R and 0 <= dy < C and v[dx][dy] == 0 and (MAP[dx][dy] == '.' or MAP[dx][dy] == 'S'):
            q.append((dx, dy, time+1, flag))
            v[dx][dy] = 1
            
print(res)