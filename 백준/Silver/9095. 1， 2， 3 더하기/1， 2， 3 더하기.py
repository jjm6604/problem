T = int(input())
for t in range(T):
    n = int(input())
    lst = [0, 1, 2, 4, 7]
    for i in range(5, n+1):
        lst.append(lst[i-1] + lst[i-2] + lst[i-3])

    print(lst[n])