def solution(scores):
    answer = 1
    wanho = scores[0]
    wanho_score = sum(wanho)
    for score in scores:
        if score[0] > wanho[0] and score[1] > wanho[1]:
            return -1
        
    scores.sort(key=lambda x:(-x[0], x[1]))
    max_score = 0
    for i in range(len(scores)):
        if scores[i][1] >= max_score:
            max_score = scores[i][1]
            if sum(scores[i]) > wanho_score:
                answer += 1
    
    return answer