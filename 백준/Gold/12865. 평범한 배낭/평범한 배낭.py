N, K = map(int, input().split())
weight = [0]
value = [0]
for i in range(N):
    a, b = map(int, input().split())
    weight.append(a)
    value.append(b)

lst = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if weight[i] <= j:
            if lst[i-1][j-weight[i]] + value[i] > lst[i-1][j]:
                lst[i][j] = lst[i-1][j-weight[i]] + value[i]
            else:
                lst[i][j] = lst[i-1][j]
        else:
            lst[i][j] = lst[i-1][j]
print(lst[N][K])