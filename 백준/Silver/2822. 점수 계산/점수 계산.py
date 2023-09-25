lst = []
for _ in range(8):
    lst.append(int(input()))
res = 0
num = []
for i in range(5):
    idx = lst.index(max(lst))
    res += lst[idx]
    lst[idx] = 0
    num.append(idx+1)
num.sort()
print(res)
print(*num)