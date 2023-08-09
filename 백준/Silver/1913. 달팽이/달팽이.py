N = int(input())
M = int(input())
lst = [[0] * N for _ in range(N)]
i = N // 2
j = N // 2
value = 1
lst[i][j] = value
result = [i+1, j+1]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
direct = 0

while value != N * N:
    i += di[direct]
    j += dj[direct]
    value += 1
    lst[i][j] = value
    if value == M:
        result = [i+1, j+1]
    if lst[i + di[(direct + 1) % 4]][j + dj[(direct + 1) % 4]] == 0:
        direct = (direct + 1) % 4
        
for l in lst:
    print(*l)
print(*result)