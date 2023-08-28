import sys

C, R = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline().strip())
lst = [[0] * R for _ in range(C)]
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
i = 0
n = 1
x, y = 0, 0
lst[0][0] = n
result = 0
if K > C * R:
    print(0)
    exit(0)
while n < K:
    nx = x + d[i][0]
    ny = y + d[i][1]
    if 0 <= nx < C and 0 <= ny < R and lst[nx][ny] == 0:
        n += 1
        lst[nx][ny] = n
        x, y = nx, ny
    else:
        i = (i+1) % 4

print(x+1, y+1)
