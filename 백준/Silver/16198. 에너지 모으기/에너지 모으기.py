def backtrack(n, s):
    if n == N-2:
        res.append(s)
        return
    for i in range(1, len(lst)-1):
        temp = lst.pop(i)
        backtrack(n+1, s + lst[i-1] * lst[i])
        lst.insert(i, temp)

N = int(input())
lst = list(map(int, input().split()))
res = []
backtrack(0, 0)
print(max(res))