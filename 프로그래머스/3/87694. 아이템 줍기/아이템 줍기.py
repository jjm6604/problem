from collections import deque

direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    K = len(rectangle)
    N, M = 0, 0
    for i in range(K):
        if rectangle[i][2] > N:
            N = rectangle[i][2]
        if rectangle[i][3] > M:
            M = rectangle[i][3]
            
    N *= 2
    M *= 2
    
    MAP = [[-1] * (M+2) for _ in range(N+2)]
    
    for i in range(K):
        X1, Y1, X2, Y2 = rectangle[i]
        for j in range(2  * X1, 2 * X2 + 1):
            MAP[j][2 * Y1] = 1
            MAP[j][2 * Y2] = 1
        for j in range(2 * Y1, 2 * Y2 + 1):
            MAP[2 * X1][j] = 1
            MAP[2 * X2][j] = 1
            
    for i in range(K):
        X1, Y1, X2, Y2 = rectangle[i]
        for j in range(2 * X1 + 1, 2 * X2):
            for k in range(2 * Y1 + 1, 2 * Y2):
                MAP[j][k] = 0
                MAP[j][k] = 0
    
            
    q = deque()
    q.append([characterX * 2, characterY * 2, 0])
    MAP[characterX * 2][characterY * 2] = 1
    
    while q:
        x, y, cnt = q.popleft()
        if itemX * 2 == x and itemY * 2 == y:
            return cnt // 2
        for d in direct:
            dx, dy = x + d[0], y + d[1]
            if 0 <= dx <= N and 0 <= dy <= M and MAP[dx][dy] == 1:
                q.append([dx, dy, cnt + 1])
                MAP[dx][dy] = 0
        
        
        
    return answer