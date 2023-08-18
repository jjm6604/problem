n = int(input())
s, e = map(int, input().split())
m = int(input())
lst = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    lst[a][b] = 1
    lst[b][a] = 1

result = -1
q = []
q.append(s)
v = [0] * (n+1)
v[s] = 1

while q and result == -1:
    x = q.pop(0)
    for i in range(n+1):
        if lst[x][i] == 1 and v[i] == 0:
            q.append(i)
            v[i] = v[x] + 1
            if i == e:
                result = v[i] - 1
                break
print(result)