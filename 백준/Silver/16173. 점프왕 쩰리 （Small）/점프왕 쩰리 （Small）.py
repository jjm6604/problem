di, dj = [1, 0], [0, 1]
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
x, y = 0, 0
v = [[0] * N for _ in range(N)]
s = []
while True:
    n = lst[x][y]
    for k in range(2):
        dx = x + di[k] * n
        dy = y + dj[k] * n
        if 0 <= dx < N and 0 <= dy < N and v[dx][dy] == 0:
            if lst[dx][dy] == -1:
                print('HaruHaru')
                exit()
            v[dx][dy] = 1
            s.append([x, y])
            x, y = dx, dy
            break

    else:
        if s:
            x, y = s.pop()
        else:
            break
print('Hing')
