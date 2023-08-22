N, K = map(int, input().split())
lst = list(map(int, input().split()))
s = 0
for i in range(K):
    s += lst[i]
sum_max = s
for i in range(K, N):
    s += lst[i]
    s -= lst[i-K]
    if sum_max < s:
        sum_max = s
print(sum_max)