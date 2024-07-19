N = int(input())
lst = [[i, *input().split()] for i in range(N)]
lst.sort(key=lambda x: (int(x[1]), x[0]))

for l in lst:
    print(*l[1:])