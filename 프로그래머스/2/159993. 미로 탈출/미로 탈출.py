from collections import deque

direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def solution(maps):
    N = len(maps)
    M = len(maps[0])
    q = deque()
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'S':
                q.append((i, j, 0, False))
                
    v = [[[0] * M for _ in range(N)] for _ in range(2)]
    answer = 0
    while q:
        x, y, n, flag = q.popleft()        
        if flag:
            if maps[x][y] == 'E':
                answer = n
                break
            for d in direct:
                dx, dy = x + d[0], y + d[1]
                if 0 <= dx < N and 0 <= dy < M and v[1][dx][dy] == 0 and maps[dx][dy] != 'X':
                    v[1][dx][dy] = 1
                    q.append((dx, dy, n+1, flag))

            
        else:
            for d in direct:
                dx, dy = x + d[0], y + d[1]
                if 0 <= dx < N and 0 <= dy < M and v[0][dx][dy] == 0 and maps[dx][dy] != 'X':
                    v[0][dx][dy] = 1
                    if maps[dx][dy] == 'L':
                        q.append((dx, dy, n+1, True))
                    else:
                        q.append((dx, dy, n+1, flag))
    if answer == 0:
        answer = -1
    
    
    
    return answer