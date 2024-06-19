from collections import deque

def solution(land):
    answer = 0
    direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    n, m = len(land), len(land[0])
    cnt = [0] * m
    v = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if v[i][j] == 0 and land[i][j] == 1:
                scope = [j, j]
                q = deque()
                v[i][j] = 1
                q.append((i, j))
                value = 0
                while q:
                    x, y = q.popleft()
                    value += 1
                    for d in direct:
                        dx, dy = x + d[0], y + d[1]
                        if 0 <= dx < n and 0 <= dy < m and v[dx][dy] == 0 and land[dx][dy] == 1:
                            v[dx][dy] = 1
                            q.append((dx, dy))
                            if dy < scope[0]:
                                scope[0] = dy
                            elif dy > scope[1]:
                                scope[1] = dy
                for k in range(scope[0], scope[1] + 1):
                    cnt[k] += value
            
    answer = max(cnt)
    return answer