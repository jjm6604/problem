def backtrack(x, y, n, cnt):
    global res
    if n > res:
        return
    if cnt == 3:
        res = n
        return
    for i in range(4):
        dx = x + direct[i][0]
        dy = y + direct[i][1]
        if 0 <= dx < 5 and 0 <= dy < 5 and v[dx][dy] == 0 and not MAP[dx][dy] == -1:

            v[dx][dy] = 1
            if MAP[dx][dy] == 0:
                backtrack(dx, dy, n+1, cnt)
            elif MAP[dx][dy] == 1:
                backtrack(dx, dy, n+1, cnt+1)
            v[dx][dy] = 0
direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]
MAP = [list(map(int, input().split())) for _ in range(5)]
v = [[0] * 5 for _ in range(5)]
x, y = map(int, input().split())
res = float('inf')
v[x][y] = 1
backtrack(x, y, 0, 0)
if res == float('inf'):
    res = -1
print(res)