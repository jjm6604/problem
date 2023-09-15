import sys
input = sys.stdin.readline
direct1 = [(1, 0), (-1, 1), (0, 1)]  # 0 2 4
direct2 = [(1, 0), (0, 1), (1, 1)] # 1 3 5

N, M = map(int, input().split())
K = int(input())
coord = [list(map(int, input().split())) for _ in range(K)]
v = [[0] * M for _ in range(N)]
# result = 0
for c in coord:
    di, dj = c
    v[di-1][dj-1] = -1
v[0][0] = 1

for j in range(M):
    for i in range(N):
        if v[i][j] == -1:
            continue
        if j % 2 == 0:
            direct = direct1
        else:
            direct = direct2
        for k in range(3):
            di = i + direct[k][0]
            dj = j + direct[k][1]
            if 0 <= di < N and 0 <= dj < M and v[di][dj] >= 0:
                v[di][dj] += v[i][j]

result = v[N-1][M-1] % (10**9 + 7)
print(result)