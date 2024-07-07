def solution(k, score):
    answer = [score[0]]
    value = min(k, len(score))
    lst = score[:value]
    lst.sort(reverse=True)
    
    for i in range(1, value):        
        if answer[i-1] < score[i]:
            answer.append(answer[i-1])
        else:
            answer.append(score[i])

            
    for i in range(k, len(score)):
        if score[i] > answer[-1]:
            lst[value-1] = score[i]
            lst.sort(reverse=True)
            answer.append(lst[value-1])
        else:
            answer.append(answer[-1])
        
    return answer