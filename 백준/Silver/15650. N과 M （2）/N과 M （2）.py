def back(k, cnt):
    if cnt == m:
        r = []
        for i in range(n):
            if x[i]:
                r.append(lst[i])
        result.append(r)
        return
    elif k == n:
        return
    x[k] = 1
    back(k+1, cnt+1)
    x[k] = 0
    back(k+1, cnt)


n, m = map(int, input().split())
lst = [i for i in range(1, n+1)]
x = [0] * n
result = []
back(0, 0)
result.sort()
for r in result:
    print(*r)