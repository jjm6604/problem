N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
result = [[0] * M for _ in range(N)]
result[0][0] = lst[0][0]
for i in range(N):
    for j in range(M):
        m = 0
        if i > 0 and m < result[i-1][j]:
            m = result[i-1][j]
        if j > 0 and m < result[i][j-1]:
            m = result[i][j-1]
        result[i][j] = m + lst[i][j]

print(result[N-1][M-1])