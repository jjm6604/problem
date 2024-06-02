lst = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

def solution(answers):
    answer = []
    scores = []
    for l in lst:
        cnt = 0
        for i in range(len(answers)):
            if l[i % len(l)] == answers[i]:
                cnt += 1
        scores.append(cnt)
    max_score = max(scores)
    for i in range(len(scores)):
        if scores[i] == max_score:
            answer.append(i+1)
    return answer