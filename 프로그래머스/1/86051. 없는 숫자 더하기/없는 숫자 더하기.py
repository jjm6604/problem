def solution(numbers):
    checked = [0] * 10
    answer = 0
    for number in numbers:
        checked[number] += 1
    for i in range(10):
        if checked[i] == 0:
            answer += i
    return answer