N = int(input())
lst = [0, 1, 2, 4, 7]
for i in range(5, N+1):
    if i % 2 == 0:
        lst.append(lst[i-1] * 2 - lst[i-4] - lst[i-5])
    else:
        lst.append(lst[i-1] * 2)
print(lst[N])