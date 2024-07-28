def solution(k, m, score):
    answer = 0
    N = len(score)
    score.sort(reverse=True)
    M = N // m
    for i in range(1, M + 1):
        answer += score[i * m - 1] * m
    return answer