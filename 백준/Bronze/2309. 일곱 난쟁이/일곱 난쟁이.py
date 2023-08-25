lst = []
for _ in range(9):
    lst.append(int(input()))
sum_v = sum(lst)
for i in range(8):
    for j in range(i+1, 9):
        if sum_v - lst[i] - lst[j] == 100:
            lst.pop(j)
            lst.pop(i)
            lst.sort()
            for l in lst:
                print(l)
            exit(0)