def backtrack(num, n):
    global C
    if n == N:
        num = int(num)
        if num > C and num < B:
            C = num
        return
    for i in range(N):
        if v[i] == 0:
            v[i] = 1
            backtrack(num + number[i], n+1)
            v[i] = 0

A, B = map(int, input().split())
N = len(str(A))
M = len(str(B))
number = str(A)
C = -1
if N > M:
    print(C)
    exit(0)

v = [0] * N
for i in range(N):
    if number[i] == '0':
        continue
    v[i] = 1
    backtrack(number[i], 1)
    v[i] = 0

print(C)
