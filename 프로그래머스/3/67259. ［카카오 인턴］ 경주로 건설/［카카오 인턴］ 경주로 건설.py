from collections import deque

direct = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def solution(board):
    answer = 0
    N = len(board)
    v = [[[float('inf')] * N for _ in range(N)] for _ in range(4)]
    q = deque()
    if board[0][1] == 0:
        v[0][0][1] = 100
        q.append([0, 0, 1])
        
    if board[1][0] == 0:
        v[1][1][0] = 100    
        q.append([1, 1, 0])
        
    while q:
        d, x, y = q.popleft()
        for i in range(4):
            dx, dy = x + direct[i][0], y + direct[i][1]
            if 0 <= dx < N and 0 <= dy < N and board[dx][dy] == 0:
                value = v[d][x][y] + 100
                if d != i:
                    value += 500
                if v[i][dx][dy] > value:
                    v[i][dx][dy] = value
                    q.append([i, dx, dy])
                    
    answer = min(v[0][-1][-1], v[1][-1][-1], v[2][-1][-1], v[3][-1][-1])
        
    
    return answer