from collections import deque

direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def solution(maps):
    answer = 0
    N, M = len(maps), len(maps[0])
    checked = [[-1] * M for _ in range(N)]
    q = deque()
    q.append([0, 0])
    checked[0][0] = 1
    while q:
        x, y = q.popleft()
        for d in direct:
            dx, dy = x + d[0], y + d[1]
            if 0 <= dx < N and 0 <= dy < M and checked[dx][dy] == -1 and maps[dx][dy] == 1:
                q.append([dx, dy])
                checked[dx][dy] = checked[x][y] + 1
    answer = checked[-1][-1]
                
    return answer