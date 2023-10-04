def backtrack(n, k):
    if n == M:
        print(*lst)
        return
    for i in range(k, N):
        lst.append(num[i])
        backtrack(n+1, i)
        lst.pop()

N, M = map(int, input().split())
num = [i for i in range(1, N+1)]
lst = []
res = set()
backtrack(0, 0)