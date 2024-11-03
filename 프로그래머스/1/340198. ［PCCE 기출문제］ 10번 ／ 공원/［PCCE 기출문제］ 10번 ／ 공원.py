def solution(mats, park):
    answer = -1
    N = len(park)
    M = len(park[0])
    max_value = -1
    
    for i in range(N):
        for j in range(M):
            if park[i][j] == "-1":
                n = 0
                flag = True
                while flag:
                    n += 1
                    if i + n == N or j + n == M:
                        break
                    for k in range(n+1):
                        if park[i+n][j+k] != "-1" or park[i+k][j+n] != "-1":
                            flag = False
                            break
                    
                if max_value < n:
                    max_value = n
                    
    for mat in mats:
        if max_value >= mat and answer < mat:
            answer = mat
                
    return answer