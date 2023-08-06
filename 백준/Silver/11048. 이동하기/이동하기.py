N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
result = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        result[i][j] = lst[i][j]
        m = 0
        if i > 0 and m < result[i-1][j]:
            m = result[i-1][j]
        if j > 0 and m < result[i][j-1]:
            m = result[i][j-1]
        if i > 0 and j > 0 and m < result[i-1][j-1]:
            m = result[i-1][j-1]
        result[i][j] += m
print(result[N-1][M-1])