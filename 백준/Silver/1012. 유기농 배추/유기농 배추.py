T = int(input())
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
for t in range(T):
    M, N, K = map(int, input().split())
    lst = [[0] * M for _ in range(N)]
    for k in range(K):
        a, b = map(int, input().split())
        lst[b][a] = 1
    v = [[0] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 1 and v[i][j] == 0:
                v[i][j] = 1
                x = i
                y = j
                l = []
                while True:
                    for k in range(4):
                        nx = x + di[k]
                        ny = y + dj[k]
                        if 0 <= nx < N and 0 <= ny < M and lst[nx][ny] == 1 and v[nx][ny] == 0:
                            v[nx][ny] = 1
                            l.append([nx, ny])
                    if len(l) == 0:
                        break
                    else:
                        x, y = l.pop()
                cnt += 1
    print(cnt)