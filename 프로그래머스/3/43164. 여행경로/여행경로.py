from collections import deque

def solution(tickets):
    answer = []
    idx = {}
    N = len(tickets)
    tickets.sort(key=lambda x: x[1])
    
    for i in range(N):
        start, end = tickets[i]
        idx[start] = idx.get(start, []) + [i]
    
    checked = [0] * N
    visited = []
    
    def travel(city, n):
        nonlocal answer
        
        if answer:
            return
        
        if n == N:
            visited.append(city)
            answer = visited[:]
            return
        
        for i in idx.get(city, []):
            if checked[i] == 0:
                checked[i] = 1
                visited.append(tickets[i][0])
                travel(tickets[i][1], n + 1)
                visited.pop()
                checked[i] = 0
                
    travel('ICN', 0)
    
    return answer