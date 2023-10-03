N = int(input())
M = int(input())
lst = list(map(int, input().split()))
res = 0
for i in range(N-1):
    for j in range(i+1, N):
        if lst[i] + lst[j] == M:
            res += 1
print(res)