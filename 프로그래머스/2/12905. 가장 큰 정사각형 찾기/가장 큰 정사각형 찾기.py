def solution(board):
    answer = 0

    N, M = len(board), len(board[0])
    k = min(N, M)
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                answer = 1
                break
                
    for i in range(1, N):
        for j in range(1, M):
            if board[i][j] == 1:
                value = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
                board[i][j] = value
                if answer < value:
                    answer = value

    return answer ** 2