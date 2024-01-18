from collections import deque

direct = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def bfs(coord, size):
    global res, fish
    q = deque()
    q.append(coord)
    visited = [[0] * N for _ in range(N)]
    lst = []
    while q:
        x, y = q.popleft()
        for i in range(4):
            dx, dy = x + direct[i][0], y + direct[i][1]
            if 0 <= dx < N and 0 <= dy < N and MAP[dx][dy] <= size and visited[dx][dy] == 0:
                visited[dx][dy] = visited[x][y] + 1
                if 0 < MAP[dx][dy] < size:
                    lst.append((dx, dy, visited[dx][dy]))
                q.append((dx, dy))
                
    if lst:
        lst.sort(key=lambda x: (x[2], x[0], x[1]))
        fish += 1
        MAP[lst[0][0]][lst[0][1]] = 0
        res += lst[0][2]
        return (lst[0][0], lst[0][1])

    return False


N = int(input())

MAP = [list(map(int, input().split())) for _ in range(N)]

res = 0
fish = 0

for i in range(N):
    for j in range(N):
        if MAP[i][j] == 9:
            point = (i, j)
            MAP[i][j] = 0

shark = 2
while point:
    point = bfs(point, shark)
    if fish == shark:
        shark += 1
        fish = 0

print(res)
