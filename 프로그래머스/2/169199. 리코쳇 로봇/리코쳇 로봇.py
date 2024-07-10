from collections import deque

direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def solution(board):
    answer = -1
    N, M = len(board), len(board[0])
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                start = [i, j]
            if board[i][j] == 'G':
                goal = [i, j]
    
    q = deque()
    q.append(start)
    v = [[-1] * M for _ in range(N)]
    v[start[0]][start[1]] = 0
    while q:
        x, y = q.popleft()
        if x == goal[0] and y == goal[1]:
            answer = v[x][y]
            break
        for d in direct:
            dx, dy = x, y
            while True:
                nx = dx + d[0]
                ny = dy + d[1]
                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != 'D':
                    dx, dy = nx, ny
                else:
                    break
            if v[dx][dy] == -1:
                v[dx][dy] = v[x][y] + 1
                q.append([dx, dy])
            
    return answer