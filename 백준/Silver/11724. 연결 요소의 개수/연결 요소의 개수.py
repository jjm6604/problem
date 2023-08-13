N, M = map(int, input().split())
lst = [[0] * (N+1) for _ in range(N+1)]

for m in range(M):
    u, v = map(int, input().split())
    lst[u][v] = 1
    lst[v][u] = 1

s = []
v = [0] * (N+1)
cnt = 0
for i in range(1, N+1):

    if v[i] == 0:
        n = i
        v[n] = 1
        while True:
            for j in range(1, N+1):
                if lst[n][j] == 1 and v[j] == 0:
                    s.append(n)
                    n = j
                    v[j] = 1
                    break
            else:
                if s:
                    n = s.pop()
                else:
                    cnt += 1
                    break
print(cnt)