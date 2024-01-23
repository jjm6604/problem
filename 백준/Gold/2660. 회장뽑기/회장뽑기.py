from collections import deque


def bfs(num):
    checked = [-1] * (N+1)
    q = deque()
    q.append(num)
    checked[num] = 0
    while q:
        x = q.popleft()
        for l in lst[x]:
            if checked[l] == -1:
                checked[l] = checked[x] + 1
                q.append(l)
    return max(checked)


N = int(input())
lst = [[] for _ in range(N+1)]
while True:
    x, y = map(int, input().split())
    if x == -1 and y == -1:
        break
    lst[x].append(y)
    lst[y].append(x)

res = [float('inf'), []]
for i in range(1, N+1):
    score = bfs(i)
    if score == res[0]:
        res[1].append(i)
    if score < res[0]:
        res[0] = score
        res[1] = [i]
print(res[0], len(res[1]))
print(*res[1])
