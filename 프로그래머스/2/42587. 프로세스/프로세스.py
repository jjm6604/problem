from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque(priorities)
    
    
    while q:
        
        max_score = max(q)
        score = q.popleft()
        if score < max_score:
            q.append(score)
            
        else:
            answer += 1
            if location == 0:
                return answer
        
        location = (location - 1) % len(q)
    return answer