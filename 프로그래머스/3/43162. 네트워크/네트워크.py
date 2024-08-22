from collections import deque


def solution(n, computers):
    answer = 0
    checked = [0] * n
    q = deque()
    for i in range(n):
        if checked[i] == 0:
            checked[i] = 1
            q.append(i)
            answer += 1
            while q:
                x = q.popleft()
                for i in range(n):
                    if computers[x][i] == 1:
                        if checked[i] == 0:
                            checked[i] = 1
                            q.append(i)
    return answer