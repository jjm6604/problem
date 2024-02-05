from collections import deque

A, B = map(int, input().split())

q = deque()
q.append((A, 1))
res = -1
nums = set()
while q:
    x, cnt = q.popleft()
    nums.add(x)
    if x == B:
        res = cnt
        break
    if x * 2 <= 10 ** 9 and x * 2 not in nums:
        q.append((x*2, cnt+1))

    if int(str(x) + '1') <= 10 ** 9 and int(str(x) + '1') not in nums:
        q.append((int(str(x) + '1'), cnt+1))
print(res)