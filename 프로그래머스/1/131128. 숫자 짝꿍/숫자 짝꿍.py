def solution(X, Y):
    answer = ''
    number = [[0] * 10 for _ in range(2)]
    for x in X:
        number[0][int(x)] += 1
    for y in Y:
        number[1][int(y)] += 1
        
    for i in range(9, -1, -1):
        if number[0][i] and number[1][i]:
            if i == 0 and not answer:
                N = 1
            else:
                N = min(number[0][i], number[1][i])
            answer += str(i) * N
            
    if not answer:
        return "-1"
    
    return answer
