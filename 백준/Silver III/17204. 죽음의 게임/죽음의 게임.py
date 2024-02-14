N, K = map(int, input().split())
lst = [0] * N
for i in range(N):
    lst[i] = int(input())
result = []
idx = 0
for _ in range(N):
    result.append(lst[idx])
    idx = lst[idx]
if K in result:
    print(result.index(K)+1)
else:
    print(-1)