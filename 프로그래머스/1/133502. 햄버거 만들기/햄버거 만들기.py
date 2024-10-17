def solution(ingredient):
    answer = 0
    N = len(ingredient)
    s = []
    for i in range(N):
        s.append(ingredient[i])
        while len(s) >= 4:
            if s[-1] == 1 and s[-2] == 3 and s[-3] == 2 and s[-4] == 1:
                answer += 1
                for j in range(4):
                    s.pop()
            else:
                break
    return answer