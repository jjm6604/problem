import heapq

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
lst = [float('inf')] * (V + 1)
lst[K] = 0
for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

q = []
heapq.heappush(q, (0, K))

while q:
    value, x = heapq.heappop(q)
    if lst[x] < value:
        continue

    for g in graph[x]:
        cost = value + g[1]
        if cost < lst[g[0]]:
            lst[g[0]] = cost
            heapq.heappush(q, (cost, g[0]))
for i in range(1, V+1):
    if lst[i] == float('inf'):
        print('INF')
    else:
        print(lst[i])