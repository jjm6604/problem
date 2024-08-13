from collections import deque

direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def solution(maps):
    answer = []
    N, M = len(maps), len(maps[0])
    q = deque()
    v = [[0] * M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if v[i][j] == 0 and maps[i][j] != 'X':
                food = int(maps[i][j])
                v[i][j] = 1 
                q = deque()
                q.append([i, j])
                while q:
                    x, y = q.popleft()
                    for d in direct:
                        dx, dy = x + d[0], y + d[1]
                        if 0 <= dx < N and 0 <= dy < M and maps[dx][dy] != 'X' and v[dx][dy] == 0:
                            q.append([dx, dy])
                            food += int(maps[dx][dy])
                            v[dx][dy] = 1
                answer.append(food)
        
    if not answer:
        return [-1]
    
    answer.sort()
    
    return answer