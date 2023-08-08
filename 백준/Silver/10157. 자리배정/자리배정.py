C, R = map(int, input().split())
# 가로 C 세로 R
K = int(input())
lst = [[0] * C for _ in range(R)]
value = 1
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
direct = 0
i, j = 0, 0
lst[i][j] = value
if K > C * R:
    print(0)
    exit()
while value != K:
    ni = i + di[direct]
    nj = j + dj[direct]
    if 0 <= ni < R and 0 <= nj < C and lst[ni][nj] == 0:
        i = ni
        j = nj
        value += 1
        lst[i][j] = value
    else:
        direct = (direct + 1) % 4

print(j+1, i+1)