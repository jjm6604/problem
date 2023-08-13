N, M = map(int, input().split())
lst = [input() for _ in range(N)]
result = 0
for i in range(N):
    cnt = 0
    if lst[i][0] == '-':
        cnt += 1
    for j in range(1, M):
        if lst[i][j-1] != '-' and lst[i][j] == '-':
            cnt += 1
    result += cnt

for i in range(M):
    cnt = 0
    if lst[0][i] == '|':
        cnt += 1
    for j in range(1, N):
        if lst[j-1][i] != '|' and lst[j][i] == '|':
            cnt += 1
    result += cnt

print(result)
