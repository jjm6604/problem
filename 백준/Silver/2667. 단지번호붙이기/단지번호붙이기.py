from collections import deque

N = int(input())
MAP = [list(map(int, input())) for _ in range(N)]

v = [[0] * N for _ in range(N)]
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

result = []
for i in range(N):
    for j in range(N):
        if MAP[i][j] == 1 and v[i][j] == 0:
            cnt = 1
            v[i][j] = 1
            q = deque()
            q.append((i, j))
            while q:
                x, y = q.popleft()
                for k in range(4):
                    di = x + d[k][0]
                    dj = y + d[k][1]
                    if 0 <= di < N and 0 <= dj < N and MAP[di][dj] == 1 and v[di][dj] == 0:
                        q.append((di, dj))
                        v[di][dj] = 1
                        cnt += 1
            result.append(cnt)

print(len(result))
result.sort()
for r in result:
    print(r)