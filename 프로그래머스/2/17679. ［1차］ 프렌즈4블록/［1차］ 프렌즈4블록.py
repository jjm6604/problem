def solution(m, n, board):
    answer = 0
    board = [list(board[i]) for i in range(m)]
    flag = True
    
    while flag:
        flag = False
        checked = [[0] * n for _ in range(m)]
        
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] and board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j] and board[i][j] == board[i+1][j+1]:
                    checked[i][j], checked[i][j+1], checked[i+1][j], checked[i+1][j+1] = 1, 1, 1, 1

        for i in range(m):
            for j in range(n):
                if checked[i][j] == 1:
                    flag = True
                    answer += 1
                    for k in range(i, 0, -1):
                        board[k][j] = board[k-1][j]
                    board[0][j] = 0
                
            
    return answer