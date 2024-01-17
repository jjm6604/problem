from collections import deque

N, M = map(int, input().split())
MAP = [0] * 100
cnt = [0] * 100

for i in range(N+M):
    x, y = map(int, input().split())
    MAP[x-1] = y-1

q = deque()
q.append(0)
while q:
    start = q.popleft()
    if start == 99:
        print(cnt[99])
    for i in range(1, 7):
        point = start + i
        if point < 100 and cnt[point] == 0:
            cnt[point] = cnt[start] + 1
            if MAP[point] != 0:
                point = MAP[point]
                if cnt[point] == 0:
                    cnt[point] = cnt[start] + 1
            q.append(point)


