def backtrack(n):
    global res
    if scores[n] == scores[n-1] == scores[n-2]:
        return
    if n == 12:
        cnt = 0
        for i in range(10):
            if lst[i] == scores[i+3]:
                cnt += 1
            if cnt == 5:
                res += 1
                return
        return
    for i in range(1, 6):
        scores.append(i)
        backtrack(n+1)
        scores.pop()
lst = list(map(int, input().split()))

scores = [-1, 0, 0]
res = 0
backtrack(2)
print(res)