def bfs(x, y):
    q = []
    q.append([x, y])
    v = [[0] * m for _ in range(n)]
    v[x][y] = 1
    result = 0
    while q:
        a, b = q.pop(0)
        for k in range(4):
            dx = a + direct[k][0]
            dy = b + direct[k][1]
            if 0 <= dx < n and 0 <= dy < m and lst[dx][dy] == 'L' and v[dx][dy] == 0:
                q.append([dx, dy])
                v[dx][dy] = v[a][b] + 1
                if result < v[dx][dy]:
                    result = v[dx][dy]
    return result

direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
n, m = map(int,input().split())
lst = [list(input()) for _ in range(n)]
r = []
for i in range(n):
    for j in range(m):
        if lst[i][j] == 'L':
            r.append(bfs(i, j))
print(max(r)-1)