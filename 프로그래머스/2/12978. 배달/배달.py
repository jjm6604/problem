import heapq

def solution(N, road, K):
    answer = 0
    result = set()
    q = []
    
    MAP = [[] for _ in range(N+1)]
    distance = [float('inf')] * (N + 1)
    for x, y, value in road:
        MAP[x].append([y, value])
        MAP[y].append([x, value])
        
    heapq.heappush(q, (0, 1))
    
    while q:
        dist, x = heapq.heappop(q)
        
        if dist > K:
            break
        
        result.add(x)
        for m in MAP[x]:
            if distance[m[0]] > dist + m[1]:
                distance[m[0]] = dist + m[1]  
                heapq.heappush(q, (dist + m[1], m[0]))
            
    answer = len(result)
    
    return answer