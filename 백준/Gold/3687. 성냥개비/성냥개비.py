T = int(input())
min_value = [8, 0, 1, 7, 4, 2, 6]
for _ in range(T):
    N = int(input())

    max_n = N // 2 - 1
    min_n = N // 7
    k = N % 7

    if N % 2 == 0:
        max_num = '1'
    else:
        max_num = '7'
    max_num += '1' * max_n

    if min_n >= 1:
        if k == 0:
            min_num = '8' * min_n
        elif k == 1:
            min_num = '10' + '8' * (min_n - 1)
        elif k == 2:
            min_num = '1' + '8' * min_n
        elif k == 3:
            if min_n == 1:
                min_num = '22'
            else:
                min_num = '2' + '0' * 2 + '8' * (min_n - 2)
        elif k == 4:
            min_num = '20' + '8' * (min_n - 1)
        elif k == 5:
            min_num = '2' + '8' * min_n
        else:
            min_num = '6' + '8' * min_n
    else:
        min_num = min_value[k]

    print(min_num, max_num)
