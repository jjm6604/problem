N = int(input())
limit_weight = list(map(int, input().split()))
M = int(input())
weight = list(map(int, input().split()))

limit_weight.sort(reverse=True)
weight.sort(reverse=True)

if limit_weight[0] < weight[0]:
    print(-1)
    exit(0)

time = 0
while weight:
    time += 1
    for i in range(N):
        for j in range(len(weight)):
            if limit_weight[i] >= weight[j]:
                weight.pop(j)
                break
print(time)