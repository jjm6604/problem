def backtrack(num, n):
    if n == N:
        nums.append(num)
        return
    backtrack(num + ' ' + str(n + 1), n + 1)
    backtrack(num + '+' + str(n + 1), n + 1)
    backtrack(num + '-' + str(n + 1), n + 1)

T = int(input())
for _ in range(T):
    N = int(input())
    nums = []
    backtrack('1', 1)
    # + 43 - 45
    for num in nums:
        s = 0
        value = '1'
        n = 1
        flag = 1
        while n < N:
            if ord(num[2 * n - 1]) == 43:
                if flag == 1:
                    s += int(value)
                else:
                    s -= int(value)
                value = ''
                flag = 1
            elif ord(num[2 * n - 1]) == 45:
                if flag == 1:
                    s += int(value)
                else:
                    s -= int(value)
                value = ''
                flag = 0

            n += 1
            value += str(n)
        if flag == 1:
            s += int(value)
        else:
            s -= int(value)
        if s == 0:
            print(num)
    print()