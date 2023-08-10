T = int(input())
for t in range(T):
    N = int(input())
    pig = list(map(int, input().split()))
    day = 1
    SUM = sum(pig)
    while N >= SUM:
        day += 1
        SUM *= 4
    print(day)