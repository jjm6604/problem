n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for i in range(n):
    for j in range(m):
        if lst[i][j] == 2:
            s = [i, j]

q = []
v = [[0] * m for _ in range(n)]
q.append(s)
v[s[0]][s[1]] = 1

while q:
    x, y = q.pop(0)
    for k in range(4):
        dx = x + direct[k][0]
        dy = y + direct[k][1]
        if 0 <= dx < n and 0 <= dy < m and lst[dx][dy] == 1 and v[dx][dy] == 0:
            q.append([dx, dy])
            v[dx][dy] = v[x][y] + 1

for i in range(n):
    for j in range(m):
        if lst[i][j] != 0:
            v[i][j] -= 1

for cnt in v:
    print(*cnt)