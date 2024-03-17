N = int(input())
lst = list(map(int, input().split()))
n = lst.pop(0)
for l in lst:
    num = l
    i = n
    k = 2
    while k <= l:
        if i % k == 0 and num % k == 0:
            i //= k
            num //= k
            continue
        k += 1
    print(f'{i}/{num}')