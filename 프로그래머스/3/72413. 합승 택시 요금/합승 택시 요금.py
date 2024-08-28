import heapq


    
def solution(n, s, a, b, fares):
    answer = float('inf')
    graph = [[] for _ in range(n+1)]
    dist = [[999999999] * (n + 1) for _ in range(n + 1)]
    for x, y, cost in fares:
        graph[x].append([y, cost])
        graph[y].append([x, cost])
        
    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        dist[start][start] = 0

        while q:
            distance, node = heapq.heappop(q)
            if distance > dist[start][node]:
                continue
            for g in graph[node]:
                new_cost = g[1] + dist[start][node]
                if new_cost < dist[start][g[0]]:
                    dist[start][g[0]] = new_cost
                    heapq.heappush(q, (new_cost, g[0]))
    for i in range(1, n+1):
        dijkstra(i)
    
    for i in range(1, n+1):
        sum_cost = dist[s][i] + dist[i][a] + dist[i][b]
        if answer > sum_cost:
            answer = sum_cost
            
    return answer


