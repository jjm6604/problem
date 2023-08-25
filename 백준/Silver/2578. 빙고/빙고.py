def func():
    result = 0
    for i in range(5):
        cnt1 = 0
        cnt2 = 0
        for j in range(5):
            if lst[i][j] == 0:
                cnt1 += 1
            if lst[j][i] == 0:
                cnt2 += 1
        if cnt1 == 5:
            result += 1
        if cnt2 == 5:
            result += 1
    cnt1 = 0
    cnt2 = 0
    for i in range(5):
        if lst[i][i] == 0:
            cnt1 += 1
        if lst[i][4-i] == 0:
            cnt2 += 1
    if cnt1 == 5:
        result += 1
    if cnt2 == 5:
        result += 1
    return result

lst = [list(map(int, input().split())) for _ in range(5)]
nums = [list(map(int, input().split())) for _ in range(5)]
cnt = 0
for num in nums:
    for n in num:
        cnt += 1
        for i in range(5):
            for j in range(5):
                if n == lst[i][j]:
                    lst[i][j] = 0
        if func() >= 3:
            print(cnt)
            exit(0)