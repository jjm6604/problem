N, M = map(int, input().split())
lst = [list(map(int, input())) for _ in range(N)]
result = 0
for i in range(N):
    for j in range(M):
        for k in range(i, N):
            for l in range(j, M):
                if lst[i][j] == lst[k][l] == lst[i][l] == lst[k][j] and k-i == l-j:
                    size = (k-i+1) * (l-j+1)
                    if result < size:
                        result = size
print(result)