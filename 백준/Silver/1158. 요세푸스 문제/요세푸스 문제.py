N, K = map(int, input().split())
lst = []
result = []
for i in range(N):
    lst.append(i+1)
cnt = K-1
while lst:
    cnt %= len(lst)
    num = lst.pop(cnt)
    result.append(num)
    cnt += K-1
print(f'<{result[0]}', end='')
for i in range(1, N):
    print(',', result[i], end='')
print('>')