from collections import deque

direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]
N, M = map(int, input().split())
start = list(map(int, input().split()))
end = list(map(int, input().split()))
MAP = [list(map(int, input().split())) for _ in range(N)]
v1 = [[0] * M for _ in range(N)]
v2 = [[0] * M for _ in range(N)]
res = -1
q = deque()
q.append((start[0]-1, start[1]-1, 0, False))
v1[start[0]-1][start[1]-1] = 1
v2[start[0]-1][start[1]-1] = 1
while q:
    x, y, cnt, flag = q.popleft()
    if (x, y) == (end[0]-1, end[1]-1):
        res = cnt
        break
    for d in direct:
        dx, dy = x + d[0], y + d[1]
        if 0 <= dx < N and 0 <= dy < M:
            if not flag and v1[dx][dy] == 0:
                if MAP[dx][dy] == 0:
                    v1[dx][dy] = cnt + 1
                    q.append((dx, dy, cnt+1, flag))
                elif MAP[dx][dy] == 1:
                    v2[dx][dy] = cnt + 1
                    q.append((dx, dy, cnt+1, True))
            if flag and v2[dx][dy] == 0 and MAP[dx][dy] == 0:
                v2[dx][dy] = cnt + 1
                q.append((dx, dy, cnt+1, flag))

print(res)