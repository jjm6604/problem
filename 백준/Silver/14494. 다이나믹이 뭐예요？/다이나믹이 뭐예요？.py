n, m = map(int, input().split())
lst = [[0] * m for _ in range(n)]
if m > 1:
    lst[0][1] = 1
if n > 1:
    lst[1][0] = 1
for i in range(n):
    lst[i][0] = 1
for i in range(m):
    lst[0][i] = 1

for i in range(1, n):
    for j in range(1, m):
        lst[i][j] = (lst[i-1][j] + lst[i][j-1] + lst[i-1][j-1]) % 1000000007

print(lst[n-1][m-1])