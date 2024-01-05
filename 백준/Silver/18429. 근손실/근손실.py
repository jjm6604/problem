def backtrack(m, s):
    global result
    if s < 500:
        return
    if m == N:
        result += 1
        return
    for i in range(N):
        if v[i] == 0:
            v[i] = 1
            backtrack(m+1, s+lst[i]-K)
            v[i] = 0

N, K = map(int, input().split())

lst = list(map(int, input().split()))
v = [0] * N
result = 0
backtrack(0, 500)
print(result)