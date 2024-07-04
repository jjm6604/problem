def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer += f'{i}' * (food[i] // 2)
    temp = answer[-1::-1]
    answer += '0' + temp
    return answer