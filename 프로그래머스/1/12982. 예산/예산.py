def solution(d, budget):
    answer = 0
    d.sort()
    
    for i in range(len(d)):
        budget -= d[i]
        if budget < 0:
            answer = i
            break
    else:
        answer = len(d)
            
    return answer