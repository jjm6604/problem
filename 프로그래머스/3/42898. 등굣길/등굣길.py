def solution(m, n, puddles):
    answer = 0
    MAP = [[0] * n for _ in range(m)]
    for x, y in puddles:
        MAP[x-1][y-1] = -1
    for i in range(n):
        if MAP[0][i] == -1:
            break
        MAP[0][i] = 1
    for i in range(m):
        if MAP[i][0] == -1:
            break
        MAP[i][0] = 1

        
    for i in range(1, m):
        for j in range(1, n):
            if MAP[i][j] == -1:
                continue
            MAP[i][j] = max(MAP[i-1][j], 0) + max(MAP[i][j-1], 0)
    
    answer = MAP[-1][-1] % 1000000007
    
    return answer