T = int(input())
for t in range(T):
    lst = [list(map(int, input().split())) for _ in range(9)]
    lst += zip(*lst)
    result = 'CORRECT'
    for i in range(18):
        cnt = [0] * 10
        for j in range(9):
            cnt[lst[i][j]] += 1

        for j in range(1, 10):
            if cnt[j] > 1:
                result = 'INCORRECT'

    for i in range(3):
        for j in range(3):
            cnt = [0] * 10
            for k in range(3):
                for l in range(3):
                    cnt[lst[3 * i + k][3 * j + l]] += 1
            for j in range(1, 10):
                if cnt[j] > 1:
                    result = 'INCORRECT'

    print(f'Case {t + 1}:', result)
    if t != T - 1:
        input()