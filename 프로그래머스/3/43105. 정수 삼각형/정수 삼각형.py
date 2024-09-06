def solution(triangle):
    answer = 0
    N = len(triangle)
    scores = [[] for _ in range(N)]
    scores[0].append(triangle[0][0])
    scores[1].append(triangle[0][0] + triangle[1][0])
    scores[1].append(triangle[0][0] + triangle[1][1])
    for i in range(2, N):
        for j in range(i+1):
            l, r = 0, 0
            if j > 0:
                l = scores[i-1][j-1]
            if j < i:
                r = scores[i-1][j]

            score = max(l, r)
            scores[i].append(score + triangle[i][j])
    answer = max(scores[-1])
    return answer