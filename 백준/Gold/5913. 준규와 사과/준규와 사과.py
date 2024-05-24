direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def backtrack(n, x, y):
    global cnt
    if n == 25 - K - 1 and x == 4 and y == 4:
        cnt += 1
        return
    nx, ny = x, y
    for d in direct:
        dx, dy = nx + d[0], ny + d[1]
        if 0 <= dx < 5 and 0 <= dy < 5 and MAP[dx][dy] == 0 and v[dx][dy] == 0:
            v[dx][dy] = 1
            backtrack(n+1, dx, dy)
            v[dx][dy] = 0


MAP = [[0] * 5 for _ in range(5)]

K = int(input())

v = [[0] * 5 for _ in range(5)]

v[0][0] = 1

for k in range(K):
    a, b = map(int, input().split())
    MAP[a-1][b-1] = 1

cnt = 0
backtrack(0, 0, 0)
print(cnt)