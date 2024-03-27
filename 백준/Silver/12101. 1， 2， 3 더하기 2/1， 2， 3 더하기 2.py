def backtrack(s):
    global cnt
    if s > N:
        return
    if s == N:
        cnt += 1
        if cnt == M:
            res = ''
            for i in range(len(lst)):
                res += '+' + str(lst[i])
            print(res[1:])
            exit()
        return
    for i in range(1, 4):
        lst.append(i)
        backtrack(s + i)
        lst.pop()


N, M = map(int, input().split())
num = set()
lst = []
cnt = 0
backtrack(0)
print(-1)