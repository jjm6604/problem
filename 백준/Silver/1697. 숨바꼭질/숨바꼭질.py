from collections import deque

N, K = map(int, input().split())
result = 0
if N >= K:
    result = N-K
else:
    coord = set()
    q = deque()
    q.append([N, 0])
    coord.add(N)
    while True:
        x, y = q.popleft()
        if x == K:
            result = y
            break
        for i in [1, -1, x]:
            dx = x + i
            if 0 <= dx <= 100000 and dx not in coord:
                q.append([dx, y+1])
                coord.add(dx)
print(result)