def solution(targets):
    answer = 1
    targets.sort(key= lambda x:x[1])
    n = targets[0][1] - 0.5
    for i in range(1, len(targets)):
        if targets[i][0] < n:
            continue
        else:
            n = targets[i][1] - 0.
            answer += 1
    
    return answer