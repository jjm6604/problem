direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def backtrack(x, y, n, cnt):
    if cnt >= 2:
        print(1)
        exit()
    if n == 3:
        return
    for i in range(4):
        dx, dy = x + direct[i][0], y + direct[i][1]
        if 0 <= dx < 5 and 0 <= dy < 5 and MAP[dx][dy] != -1:
            MAP[x][y] = -1
            if MAP[dx][dy] == 1:
                backtrack(dx, dy, n+1, cnt+1)
            else:
                backtrack(dx, dy, n+1, cnt)
            MAP[x][y] = 0


MAP =[list(map(int, input().split())) for _ in range(5)]
x, y = map(int, input().split())

backtrack(x, y, 0, 0)
print(0)