def backtrack(n, s):
    global res
    if n == 11:
        if res < s:
            res = s
        return
    for i in range(11):
        if v[i] == 0 and MAP[n][i] != 0:
            v[i] = 1
            backtrack(n+1, s + MAP[n][i])
            v[i] = 0

            
T = int(input())
for _ in range(T):
    MAP = [list(map(int, input().split())) for _ in range(11)]
    res = 0
    v = [0] * 11
    backtrack(0, 0)
    print(res)