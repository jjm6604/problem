direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]
N = int(input())
lst = [list(map(int, input())) for _ in range(N)]
result = []
# N * N
v = [[0] * N for _ in range(N)]
s = []
for i in range(N):
    for j in range(N):
        if lst[i][j] == 1 and v[i][j] == 0:
            cnt = 1
            v[i][j] = 1
            x = i
            y = j
            while True:
                for k in range(4):
                    dx = x + direct[k][0]
                    dy = y + direct[k][1]
                    if 0 <= dx < N and 0 <= dy < N and lst[dx][dy] == 1 and v[dx][dy] == 0:
                        s.append([dx, dy])
                        v[dx][dy] = 1
                        cnt += 1
                else:
                    if s:
                        x, y = s.pop()
                    else:
                        result.append(cnt)
                        break
result.sort()
print(len(result))
for r in result:
    print(r)
