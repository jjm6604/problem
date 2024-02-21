direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def dfs(x, y, n, num):
    if n == 6:
        res.add(num)
        return
    for d in direct:
        dx, dy = x + d[0], y + d[1]
        if 0 <= dx < 5 and 0 <= dy < 5:
            dfs(dx, dy, n+1, num+str(MAP[dx][dy]))

MAP = [list(map(int, input().split())) for _ in range(5)]

res = set()
for i in range(5):
    for j in range(5):
        dfs(i, j,0, '')

print(len(res))