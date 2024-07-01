from collections import deque

def solution(numbers, target):
    answer = 0
    cnt = 0
    q = deque()
    q.append([0, 0, 0])
    q.append([0, 0, 1])
    while q:
        value, n, flag = q.popleft()
        if n == (len(numbers)):
            if value == target:
                answer += 1
        else:
            if flag:
                q.append([value + numbers[n], n + 1, 0])
                q.append([value + numbers[n], n + 1, 1])
            else:
                q.append([value - numbers[n], n + 1, 0])
                q.append([value - numbers[n], n + 1, 1])
    answer //= 2
    return answer