from collections import deque

T = int(input())
for t in range(T):
    S, T = map(int, input().split())
    q = deque()
    q.append((S, T, 0))
    while q:
        s, t, cnt = q.popleft()
        if s == t:
            print(cnt)
            break
        q.append((s + 1, t, cnt + 1))
        if s * 2 <= t + 3:
            q.append((s * 2, t + 3, cnt + 1))
