m = int(input())
n = int(input())

lst = [[] for _ in range(m)]

for _ in range(n):
    a, b = map(int, input().split())
    lst[a-1].append(b-1)
    lst[b-1].append(a-1)

v = [0] * m
q = [0]
v[0] = 1
while q:
    x = q.pop(0)
    for a in lst[x]:
        if v[a] == 0:
            q.append(a)
            v[a] = 1
result = v[1:].count(1)

print(result)
