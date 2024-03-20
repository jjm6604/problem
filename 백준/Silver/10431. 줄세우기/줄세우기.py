P = int(input())

for _ in range(P):
    lst = list(map(int, input().split()))
    new_lst = [lst[1]]
    res = 0
    for i in range(2, 21):
        for j in range(len(new_lst)):
            if new_lst[j] > lst[i]:
                new_lst.insert(j, lst[i])
                res += len(new_lst) - 1 - j
                break
        else:
            new_lst.append(lst[i])


    print(lst[0], res)