def solution(numbers):
    answer = []
    result = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            result.add(numbers[i]+numbers[j])
    answer = list(result)
    answer.sort()
    return answer