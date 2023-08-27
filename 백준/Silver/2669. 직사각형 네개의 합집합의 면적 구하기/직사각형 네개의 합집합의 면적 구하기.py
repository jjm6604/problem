num = [list(map(int, input().split())) for _ in range(4)]
lst = [[0] * 101 for _ in range(100)]

for i in range(4):
    for j in range(num[i][0], num[i][2]):
        for k in range(num[i][1], num[i][3]):
            lst[j][k] = 1
cnt = 0
for i in range(100):
    for j in range(100):
        if lst[i][j] == 1:
            cnt += 1
print(cnt)