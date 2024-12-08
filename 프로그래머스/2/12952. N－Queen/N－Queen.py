def solution(n):
    answer = 0
    board = [[0] * n for _ in range(n)]
    diagonal1 = [0] * (2 * n - 1)
    diagonal2 = [0] * (2 * n - 1)
    def checking(x, y):
        for i in range(n):
            if (i != y and board[x][i] == 1) or (i != x and board[i][y] == 1):
                return False
        
            
        return True
    
    def nQueen(k):
        nonlocal answer
        if k == n:
            answer += 1
            return
        for i in range(n):
            if not diagonal1[k+i] and not diagonal2[k-i]:
                board[k][i] = 1
                diagonal1[k+i] = 1
                diagonal2[k-i] = 1
                if checking(k, i):
                    nQueen(k+1)
                board[k][i] = 0
                diagonal1[k+i] = 0
                diagonal2[k-i] = 0
    nQueen(0)
    return answer
