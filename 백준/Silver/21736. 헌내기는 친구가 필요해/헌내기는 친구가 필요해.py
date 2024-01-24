from collections import deque

direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]

N, M = map(int, input().split())
MAP = [input() for _ in range(N)]
visited = [[0] * M for _ in range(N)]
result = 0
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 'I':
            start = (i, j)
            visited[i][j] = 1
            break
    else:
        continue
    break

q = deque()
q.append(start)

while q:
    x, y = q.popleft()
    for i in range(4):
        dx, dy = x + direct[i][0], y + direct[i][1]
        if 0 <= dx < N and 0 <= dy < M and visited[dx][dy] == 0 and MAP[dx][dy] != 'X':
            visited[dx][dy] = 1
            if MAP[dx][dy] == 'P':
                result += 1
            q.append((dx, dy))

if result:
    print(result)
else:
    print('TT')