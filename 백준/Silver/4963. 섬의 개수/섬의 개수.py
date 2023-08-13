di = [1, 0, -1, 0, 1, 1, -1, -1]
dj = [0, 1, 0, -1, 1, -1, -1, 1]
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    MAP = [list(map(int, input().split())) for _ in range(h)]
    # h * w
    # 1 땅 0 바다
    cnt = 0
    v = [[0] * w for _ in range(h)]
    s = []
    for i in range(h):
        for j in range(w):
            if MAP[i][j] == 1 and v[i][j] == 0:
                v[i][j] = 1
                x = i
                y = j
                lst = []
                while True:
                    for k in range(8):
                        nx = x + di[k]
                        ny = y + dj[k]
                        if 0 <= nx < h and 0 <= ny < w and MAP[nx][ny] == 1 and v[nx][ny] == 0:
                            v[nx][ny] = 1
                            lst.append([nx, ny])
                    if lst:
                        x, y = lst.pop()
                    else:
                        break
                cnt += 1
    print(cnt)
