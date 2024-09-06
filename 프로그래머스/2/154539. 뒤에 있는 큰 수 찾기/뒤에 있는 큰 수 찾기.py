def solution(numbers):
    answer = [-1]
    N = len(numbers)
    num = numbers[-1]
    for i in range(N-2, -1, -1):
        if numbers[i] < num:
            answer.append(num)
        else:
            for j in range(N-2-i, -1, -1):
                if answer[j] > numbers[i] or answer[j] == -1:
                    answer.append(answer[j])
                    break
        num = numbers[i]
    answer = answer[::-1]
    return answer