N = int(input())
lst = list(map(int, input().split()))
K = int(input())
for _ in range(K):
    a, b = map(int, input().split())
    if a == 1:
        n = b-1
        while n < N:
            lst[n] = 1 if lst[n] == 0 else 0
            n += b
    else:
        n = 1
        b -= 1
        lst[b] = 1 if lst[b] == 0 else 0
        while 1:

            if (0 <= b-n and b+n < N) and (lst[b-n] == lst[b+n]):
                lst[b-n] = 1 if lst[b-n] == 0 else 0
                lst[b+n] = lst[b-n]
                n += 1
            else:
                break
for i in range(len(lst)):
    print(lst[i], end=' ')
    if (i+1) % 20 == 0:
        print()