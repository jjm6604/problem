from collections import deque


N = int(input())
lst = list(map(int, input().split()))
S = int(input()) - 1
visited = [0] * N
q = deque()
visited[S] = 1
cnt = 1
q.append(S)

while q:
    x = q.popleft()
    for i in [lst[x], -lst[x]]:
        dx = x + i
        if 0 <= dx < N and visited[dx] == 0:
            visited[dx] = 1
            cnt += 1
            q.append(dx)
print(cnt)