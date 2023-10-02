def backtrack(n):
    if n == M:
        print(*lst)
        return
    for i in range(N):
        lst.append(num[i])
        backtrack(n+1)
        lst.pop()

        
N, M = map(int, input().split())
num = [i for i in range(1, N+1)]
lst = []
backtrack(0)