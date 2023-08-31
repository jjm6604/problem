N = int(input())
lst = []
for i in range(N):
    s, e = map(int, input().split())
    lst.append([s, e])
lst.sort(key=lambda x:x[1])
lst.sort(key=lambda x:x[0])
selects = [lst[0]]
for i in range(1, N):
    if lst[i][0] >= selects[-1][1]:
        selects.append(lst[i])
    elif lst[i][1] < selects[-1][1]:
        selects[-1] = lst[i]
result = len(selects)
print(result)