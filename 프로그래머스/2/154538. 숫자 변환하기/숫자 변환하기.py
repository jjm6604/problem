from collections import deque

def solution(x, y, n):
    answer = -1
    checked = set()
    q = deque()
    
    checked.add(x)
    q.append([x, 0])
    
    while q:
        number, cnt = q.popleft()
        if number == y:
            return cnt
        for i in [n, number, 2 * number]:
            value = number + i
            if 1 <= value <= 1000000 and value not in checked:
                checked.add(value)
                q.append([value, cnt + 1])
                
    return answer