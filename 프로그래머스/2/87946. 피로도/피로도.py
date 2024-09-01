def solution(k, dungeons):
    answer = -1
    N = len(dungeons)
    
    checked = [0] * N
    
    def backtrack(HP, cnt):
        nonlocal answer
        
        if cnt > answer:
            answer = cnt
            
        for i in range(N):
            if checked[i] == 0 and HP >= dungeons[i][0]:
                checked[i] = 1
                backtrack(HP - dungeons[i][1], cnt + 1)
                checked[i] = 0
                
    backtrack(k, 0)
    
    return answer
    
    