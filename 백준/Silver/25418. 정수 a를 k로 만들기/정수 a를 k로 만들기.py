from collections import deque

A, K = map(int, input().split())
q = deque()
q.append((A, 0))
nums = set()

while q:
    x, cnt = q.popleft()
    if x == K:
        print(cnt)
        break
    for i in [1, x]:
        dx = x + i
        if dx not in nums and 1 <= dx <= 1000000:
            nums.add(dx)
            q.append((dx, cnt+1))