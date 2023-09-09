N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(M)]
value1, value2 = lst[0]
for i in range(1, M):
    if value1 > lst[i][0]:
        value1 = lst[i][0]
    if value2 > lst[i][1]:
        value2 = lst[i][1]
result = value2 * N
for i in range(1, N//6+2):
    n = (N-6*i) if N-6*i > 0 else 0
    if value1 * i + value2 * n < result:
        result = value1 * i + value2 * n
print(result)