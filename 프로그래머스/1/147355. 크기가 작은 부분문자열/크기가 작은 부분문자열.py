def solution(t, p):
    answer = 0
    N, M = len(t), len(p)
    number1 = int(p)
    for i in range(N-M+1):
        number2 = int(t[i:i+M])
        if number2 <= number1:
            answer += 1
    return answer