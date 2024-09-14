def solution(array, commands):
    answer = []
    
    for i, j, k in commands:
        numbers = array[i-1: j]
        numbers.sort()

        answer.append(numbers[k - 1])
    
    return answer