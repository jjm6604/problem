N = int(input())
M = int(input())
lst = [[0] * (N+1) for _ in range(N+1)]
for m in range(M):
    a, b = map(int, input().split())
    lst[a][b] = 1
    lst[b][a] = 1

n = 1
s = []
v = [0] * (N+1)
v[n] = 1
while True:
    for i in range(N+1):
        if lst[n][i] == 1 and v[i] == 0:
            s.append(n)
            n = i
            v[n] = 1
            break
    else:
        if s:
            n = s.pop()
        else:
            break
print(v[2:].count(1))
