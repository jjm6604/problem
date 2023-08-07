N, K = map(int,input().split())
lst = []

for i in range(2, N+1):
    lst.append(i)

cnt = 0
while True:
    num = lst[0]
    value = 1
    while num * value <= N:
        remove_value = num * value
        if remove_value in lst:
            lst.remove(remove_value)
            cnt += 1
        value += 1
        if cnt == K:
            result = remove_value
            break
    if cnt != K:
        continue
    else:
        break
print(remove_value)