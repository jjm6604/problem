def backtrack(n):
    if n == N:
        print(*lst)
        return

    for i in range(1, N+1):
        if checked[i] == 0:
            checked[i] = 1
            lst.append(i)
            backtrack(n+1)
            checked[i] = 0
            lst.pop()

N = int(input())

lst = []
checked = [0] * (N+1)
backtrack(0)