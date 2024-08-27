def solution(land):
    answer = 0
    N = len(land)
    score = [[0] * 4 for _ in range(N)]
    score[0] = land[0][:]
    
    for i in range(1, N):
        score[i][0] = max(score[i-1][1], score[i-1][2], score[i-1][3]) + land[i][0]
        score[i][1] = max(score[i-1][0], score[i-1][2], score[i-1][3]) + land[i][1]     
        score[i][2] = max(score[i-1][0], score[i-1][1], score[i-1][3]) + land[i][2]     
        score[i][3] = max(score[i-1][0], score[i-1][1], score[i-1][2]) + land[i][3]
    answer = max(score[-1])
    return answer