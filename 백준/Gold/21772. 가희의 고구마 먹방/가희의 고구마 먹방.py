direct = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def backtrack(x, y, n, cnt):
    res.add(cnt)
    if n == T:
        return
    for i in range(4):
        dx, dy = x + direct[i][0], y + direct[i][1]
        if 0 <= dx < N and 0 <= dy < M and MAP[dx][dy] != '#':

            if MAP[dx][dy] == 'S':
                MAP[dx][dy] = '.'
                backtrack(dx, dy, n + 1, cnt + 1)
                MAP[dx][dy] = 'S'
            else:
                backtrack(dx, dy, n + 1, cnt)


N, M, T = map(int, input().split())
MAP = [list(input()) for _ in range(N)]
res = set()
res.add(0)

for i in range(N):
    for j in range(M):
        if MAP[i][j] == 'G':
            start = (i, j, 0, 0)

backtrack(*start)
print(max(res))