N = int(input())
lst = [0, 0, 1, 3]
for i in range(4, N+1):
    num = (i // 2) * (i // 2 if i % 2 == 0 else i // 2 + 1)
    lst.append(num + lst[i//2] + lst[(i // 2 if i % 2 == 0 else i // 2 + 1)])
print(lst[N])