T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    X = int(input().replace(' ', ''))
    Y = int(input().replace(' ', ''))
    lst = list(map(int, input().split()))

    lst += lst[:M]
    cnt = 0
    for i in range(N):
        num = 0
        for j in range(M):
            num = (num * 10) + lst[i+j]
        if X <= num <= Y:
            cnt += 1

    print(cnt)