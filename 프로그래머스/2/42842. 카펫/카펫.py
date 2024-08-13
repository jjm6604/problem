def solution(brown, yellow):
    answer = []
    number = brown + yellow
    lst = []

    for i in range(3, int(number ** 0.5) + 1):
        if number % i == 0:
            lst.append([number//i, i])

    for l in lst:
        if (l[0] - 2) * (l[1] - 2) == yellow:
            answer = l
            break
            
    return answer