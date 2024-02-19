from collections import deque

damages = [(9, 3, 1), (9, 1, 3), (1, 3, 9), (1, 9, 3), (3, 1, 9), (3, 9, 1)]
N = int(input())
lst = list(map(int, input().split()))
while len(lst) < 3:
    lst.append(0)
q = deque()
nums = set()
lst.sort()
q.append((*lst, 0))
while q:
    a, b, c, cnt = q.popleft()
    if a <= 0 and b <= 0 and c <= 0:
        print(cnt)
        break
    for damage in damages:
        na, nb, nc = a - damage[0], b - damage[1], c - damage[2]
        lst = (na, nb, nc)
        if lst not in nums:
            nums.add(lst)
            q.append((*lst, cnt+1))