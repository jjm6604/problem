from collections import deque

def solution(stones, k):
    answer = float('inf')
    N = len(stones)
    n = -1
    value = deque()
    value.append(-1)
    
    for i in range(N):
        if value and value[0] < i - k + 1:
            value.popleft()
        
        while value and stones[value[-1]] <= stones[i]:
            value.pop()
            
        value.append(i)
        
        if i >= k - 1:
            answer = min(answer, stones[value[0]])
        
        
    return answer