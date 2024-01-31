from collections import deque

direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]
N, M = map(int, input().split())

MAP = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 2:
            start = (i, j, 0)
            break
    else:
        continue
    break

q = deque()
q.append(start)
visited[start[0]][start[1]] = 1


while q:
    x, y, cnt = q.popleft()
    for i in range(4):
        dx, dy = x + direct[i][0], y + direct[i][1]
        if 0 <= dx < N and 0 <= dy < M and visited[dx][dy] == 0 and MAP[dx][dy] != 1:
            if MAP[dx][dy] in [3, 4, 5]:
                print("TAK")
                print(cnt+1)
                exit()
            visited[dx][dy] = 1
            q.append((dx, dy, cnt+1))

print("NIE")
