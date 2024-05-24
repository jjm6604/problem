from collections import deque

n = int(input())
m = int(input())

bus = [[] for _ in range(n+1)]
result = [[float('inf')] * (n+1) for _ in range(n+1)]
for i in range(m):
    start, end, cost = map(int, input().split())
    bus[start].append([end, cost])

for i in range(1, n+1):
    s = []
    s.append([i, 0])
    while True:

        x, money = s.pop()
        for b in bus[x]:
            if result[i][b[0]] > money + b[1]:
                result[i][b[0]] = money + b[1]
                s.append([b[0], money + b[1]])
        else:
            if s:
                continue

            else:
                break

for i in range(1, n+1):
    for j in range(1, n+1):
        if result[i][j] == float('inf'):
            result[i][j] = 0
    result[i][i] = 0

for i in range(1, n+1):
    print(*result[i][1:])