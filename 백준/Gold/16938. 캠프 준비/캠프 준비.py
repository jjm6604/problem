def backtrack(n, m):
    global res
    if sum(selected) > R:
        return

    if n == N:
        if len(selected) >= 2 and sum(selected) >= L and (max(selected) - min(selected) >= X):
            res += 1
        return

    selected.append(lst[n])
    backtrack(n+1, m+1)
    selected.pop()
    backtrack(n+1, m)


N, L, R, X = map(int, input().split())
lst = list(map(int, input().split()))
selected = []
res = 0
backtrack(0, 0)
print(res)