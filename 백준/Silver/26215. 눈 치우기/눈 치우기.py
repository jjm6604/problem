N = int(input())
lst = list(map(int, input().split()))

res = 0

sum_time = sum(lst)
max_time = max(lst)
if sum_time > 2 * max_time:
    res = sum_time // 2
    if sum_time % 2 == 1:
        res += 1

else:
    res = max_time

if res > 1440:
    print(-1)
else:
    print(res)